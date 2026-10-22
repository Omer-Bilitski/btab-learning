"""Package the owner's approved maintenance changes only; no remote writes."""
import hashlib
import json
from pathlib import Path
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'dist'
out.mkdir(parents=True, exist_ok=True)
manifest = json.loads((root / 'plugin.json').read_text(encoding='utf-8'))
assert manifest['name'] == 'btab-learning' and manifest['version'] == '1.2.6'
skills = root / 'skills'
assert len(list(skills.glob('*/SKILL.md'))) == 5
for p in skills.rglob('*'):
    if p.is_file():
        assert p.read_bytes() == (root / 'plugins/btab-learning' / p.relative_to(root)).read_bytes(), p
        if p.suffix == '.md':
            assert 'package version 1.2.1' not in p.read_text(encoding='utf-8')
standalone = (skills / 'check-my-work/SKILL.md').read_text(encoding='utf-8')
reference = (skills / 'btab-learning/references/check-my-work.md').read_text(encoding='utf-8')
normalize = lambda text: text.replace('\r\n', '\n')
assert normalize(standalone.split('## Personal explanation preferences')[1]) == normalize(reference.split('## Personal explanation preferences')[1])
for text in (standalone, reference):
    assert 'When GitHub tools are available' not in text
    assert 'does not write observations to external services' in text
    assert 'Prefer an additive annotation layer' in text
    assert 'meaning does not depend on color alone' in text
    assert 'return a copy annotated in red' in text
    assert 'Do not silently fall back to text' in text
    assert 'For an attempt supplied only as text or equations' in text
    assert 'attempt the annotation before finalizing' in text
    assert 'Never invent account, model, plan, quota, or platform restrictions' in text
assert 'Do not wait for permission between them.' in (skills / 'solve-then-explain/SKILL.md').read_text(encoding='utf-8')

def archive(name, entries):
    path = out / name
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for target, source in sorted(entries):
            info = zipfile.ZipInfo(target, date_time=(2026, 10, 22, 0, 0, 0))
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, source.read_bytes())
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
    return path

files = [p for p in skills.rglob('*') if p.is_file()]
artifacts = [archive('btab-learning-v1.2.6.zip', [('btab-learning/plugin.json', root / 'plugin.json')] + [('btab-learning/' + p.relative_to(root).as_posix(), p) for p in files])]
artifacts.append(archive('btab-learning-skill-v1.2.6.zip', [('btab-learning/' + p.relative_to(skills / 'btab-learning').as_posix(), p) for p in (skills / 'btab-learning').rglob('*') if p.is_file()]))
artifacts.append(archive('check-my-work-v1.2.6.zip', [('check-my-work/' + p.relative_to(skills / 'check-my-work').as_posix(), p) for p in (skills / 'check-my-work').rglob('*') if p.is_file()]))
(out / 'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.name + '\n' for p in artifacts), encoding='utf-8', newline="\n")
print(json.dumps({'version': '1.2.6', 'skills': 5, 'files': len(files) + 1, 'artifacts': [p.name for p in artifacts], 'checks': 'passed'}))
