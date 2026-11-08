#!/usr/bin/env python3
"""기록 옮기기를 index.html에 넣는다. pipeline/record-transfer/build.cjs와 같은 결과를 내는 파이썬판(26.11.09).

왜 따로 있나: 이 저장소를 고치는 맥미니에는 node가 없다. 같이 쓰는 파일(merge.js·runtime.js·ui.html·style.css·build.cjs)은
보카고양 본가 것을 그대로 두고(SHARED.md), 넣는 일만 파이썬으로 한다. node가 있는 곳에서 `node pipeline/record-transfer/build.cjs --check`가
통과해야 한다(같은 글자를 만든다).
사용: python3 -I pipeline/record_transfer_build.py [--check]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / 'pipeline' / 'record-transfer'


def read(p):
    return p.read_text(encoding='utf-8').replace('\r\n', '\n')


def src(name):
    return read(HERE / name).strip()


def build(html):
    config = json.loads(read(HERE / 'config.json'))
    css = '<style id="record-transfer-style">\n' + src('style.css') + '\n</style>'
    if '<style id="record-transfer-style">' in html:
        html = re.sub(r'<style id="record-transfer-style">[\s\S]*?</style>', lambda m: css, html, count=1)
    else:
        html = html.replace('</head>', css + '\n</head>', 1)
    ui = '<!-- RECORD_TRANSFER_UI_START -->\n' + src('ui.html') + '\n  <!-- RECORD_TRANSFER_UI_END -->'
    if '<!-- RECORD_TRANSFER_UI_START -->' in html:
        html = re.sub(r'<!-- RECORD_TRANSFER_UI_START -->[\s\S]*?<!-- RECORD_TRANSFER_UI_END -->', lambda m: ui, html, count=1)
    else:
        at = html.find('  <div class="foot">')
        assert at >= 0, 'index.html foot'
        html = html[:at] + '  ' + ui + '\n\n' + html[at:]
    cfg = {k: v for k, v in config.items() if k != 'about'}
    merge = re.sub(r'\nif\(typeof module[^\n]*\Z', '', src('merge.js'))
    js = ('<script id="record-transfer">\n/* RECORD_TRANSFER_START */\nvar RT_CONFIG=' + json.dumps(cfg, ensure_ascii=False, separators=(',', ':'))
          + ';\n' + merge + '\n' + src('runtime.js') + '\n/* RECORD_TRANSFER_END */\n</script>')
    if '<script id="record-transfer">' in html:
        html = re.sub(r'<script id="record-transfer">[\s\S]*?</script>', lambda m: js, html, count=1)
    else:
        html = html.replace('</body>', js + '\n</body>', 1)
    return html


if __name__ == '__main__':
    target = ROOT / json.loads(read(HERE / 'config.json'))['target']
    before = read(target)
    after = build(before)
    if '--check' in sys.argv:
        sys.exit(0 if before == after else target.name + ' 기록 옮기기 코드가 낡았다')
    target.write_text(after, encoding='utf-8')
    print('Updated', target.name)
