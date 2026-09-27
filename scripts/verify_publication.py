"""Verify preserved research bytes and replay the immutable original release.

Publication overlays are explicitly excluded from the original-byte comparison;
the original archive verifier is never relaxed or rewritten.
"""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, tempfile, urllib.request, zipfile
ROOT=Path(__file__).resolve().parents[1]
CONFIG={'repo': 'Auditable-Flourishing', 'sha256': 'cfd1b7a38a0320dc9b4d267947f4ba29fbc5469fe189166cd0a3624ea21cfef6', 'root': 'Auditable_Flourishing_v6_2_COMPLETE_READY', 'verifier': 'verify_release_v6_2.py', 'overlay': ['README.md'], 'url': 'https://github.com/MathGov/Auditable-Flourishing/releases/download/AF-v6.2/Auditable_Flourishing_v6_2_COMPLETE_READY_MASTER_PACKAGE_FINAL.zip'}
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--archive', type=Path, help='Use a previously downloaded original ZIP')
    args=parser.parse_args()
    original=json.loads((ROOT/'provenance/ORIGINAL_REPOSITORY_SHA256.json').read_text(encoding='utf-8'))
    failed=[]
    for name, expected in original.items():
        if name in CONFIG['overlay']: continue
        p=ROOT/name
        if not p.is_file():
            failed.append(name); continue
        data=p.read_bytes()
        if expected['normalize_crlf']: data=data.replace(b'\r\n',b'\n')
        if hashlib.sha256(data).hexdigest()!=expected['sha256']: failed.append(name)
    if failed: raise SystemExit('Preserved-file mismatch: '+', '.join(failed))
    print('PASS: preserved repository payload',len(original)-len(CONFIG['overlay']),'files',flush=True)
    with tempfile.TemporaryDirectory(prefix='publication-verify-') as tmp:
        tmp=Path(tmp)
        archive=args.archive.resolve() if args.archive else tmp/'original.zip'
        if not args.archive:
            urllib.request.urlretrieve(CONFIG['url'],archive)
        if digest(archive)!=CONFIG['sha256']: raise SystemExit('Original archive SHA-256 mismatch')
        target=tmp/'extracted'
        target.mkdir()
        with zipfile.ZipFile(archive) as z:
            for member in z.infolist():
                if not (target/member.filename).resolve().is_relative_to(target.resolve()):
                    raise SystemExit('Unsafe archive member')
            z.extractall(target)
        package=target/CONFIG['root']
        command=[sys.executable,'-B',str(package/CONFIG['verifier'])]
        if CONFIG['repo']=='AIAP': command.append(str(package))
        subprocess.run(command,cwd=package,check=True)
    if CONFIG['repo']=='AIAP':
        subprocess.run([sys.executable,'-B','-m','unittest','-v','test_validate_aiap_record.py'],cwd=ROOT/'06_MACHINE_READABLE',check=True)
    print('PASS: publication integrity and original release verification; not empirical validation.')
if __name__=='__main__': main()
