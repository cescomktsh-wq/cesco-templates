# -*- coding: utf-8 -*-
"""클릭 없이 한 번에 보는 정적 비교: 치킨집·산후조리원 × (선택 항목 10개 + 수치형·인터뷰형·상세페이지형). 기본 템플릿 상태(사장님 수정 없음).
실행: python3 reports/261028/scripts/build_static.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import build as B, build_tpl as T

OUT = os.path.join(os.path.dirname(__file__), '..')
FNAME = 'wecheck_draft_261028.html'
TYPES = [('A','수치형','세스코 실측 계기판 아래 "이 집은 ~"으로 사장님 문장이 붙음'),('B','인터뷰형','고른 항목이 질문, 사장님 문장이 답 (셀프 인터뷰)'),('C','상세페이지형','풀블리드 사진 + POINT 01~03')]

CSS = r"""
.bizsec{max-width:1320px;margin:0 auto;padding:10px 20px 40px}
.bizsec h2{margin:0 0 4px;font-size:18px;font-weight:900;color:var(--ink)}
.bizsec .sub{font-size:12.5px;color:var(--muted);margin-bottom:14px}
.opts{background:#fff;border-radius:12px;padding:14px 18px;margin-bottom:18px}
.opts h3{margin:0 0 8px;font-size:13.5px;font-weight:900;color:var(--ink)}
.opts h3 small{font-weight:600;color:var(--muted);font-size:11.5px;margin-left:8px}
.opts .tw{overflow-x:auto}
.opts table{width:100%;min-width:720px;border-collapse:collapse;font-size:12px}
.opts th,.opts td{border-top:1px solid var(--line);padding:7px 8px;text-align:left;vertical-align:top;line-height:1.5}
.opts th{font-size:11px;color:var(--muted);font-weight:800;border-top:0;white-space:nowrap}
.opts td.n{width:26px;font-weight:900;color:var(--ink)}
.opts tr.sel td{background:var(--wc-bg)}
.opts td .pick{display:inline-block;font-size:9.5px;font-weight:900;color:#fff;background:var(--wc);border-radius:999px;padding:1px 7px;margin-right:4px}
.opts td .cs{font-size:10px;font-weight:800;color:var(--wc);white-space:nowrap}
.opts td .cs.o{color:var(--muted)}
.opts td.cp{color:var(--txt)}
.row3{display:flex;gap:20px;align-items:flex-start;justify-content:center;flex-wrap:wrap}
.row3 .ed{width:390px}
@media (max-width:760px){.row3 .ed{width:100%}}
.row3 figure{margin:0;width:390px;max-width:100%;min-width:0}
.row3 figcaption b{display:block;font-size:13px}
.row3 figcaption small{font-size:11px}
@media (max-width:760px){.bizsec{padding:10px 0 30px}.opts{border-radius:0}.row3{gap:14px}}
"""

def opts_table(bk):
    t = T.TPL[bk]; sel = t['default_sel']
    rows = ''
    for i, (label, title, copy, chip, cesco) in enumerate(t['items']):
        q = T.QS[bk][i]
        on = i in sel
        pick = f'<span class="pick">기본 선택 {sel.index(i)+1}</span>' if on else ''
        rows += f'<tr class="{"sel" if on else ""}"><td class="n">{i+1}</td><td>{pick}<b>{label}</b><br><span class="cs{"" if cesco else " o"}">{"세스코 점검 항목" if cesco else "매장 기록"}</span></td><td>{title.replace("<br>"," ")}</td><td class="cp">{copy}</td><td class="cp">{q}</td></tr>'
    return f'<div class="opts"><h3>{t["owner"]} 선택 항목 {len(t["items"])}개<small>2~3개 선택 · 고른 순서대로 노출 · 파란 줄이 기본 선택(사장님이 아무것도 안 골랐을 때)</small></h3><div class="tw"><table><thead><tr><th>#</th><th style="width:19%">항목</th><th style="width:17%">제목 (고정)</th><th>기본 설명 (사장님 수정 가능 · 140자)</th><th style="width:20%">인터뷰형 질문</th></tr></thead><tbody>{rows}</tbody></table></div></div>'

def build():
    secs = ''
    for bk in ['chicken', 'care']:
        t = T.TPL[bk]; reg = t['reg']
        figs = f'<figure><figcaption><b>{t["owner"]} 선택 화면</b><small>위쳌 사업주용 · 2~3개 체크 · 기본 문안이 미리 들어 있음 · 여기서 바꾸면 오른쪽 3개가 같이 바뀜</small></figcaption><div class="ed"><div class="bar">위생 페이지 관리<span class="sv">저장</span></div><div class="in" data-ed data-biz="{bk}"></div></div></figure>'
        for code, nm, ds in TYPES:
            figs += f'<figure><figcaption><b>{nm}</b><small>{ds}</small></figcaption><div class="phone"><div class="fold"><span>첫 화면 끝</span></div><div data-static data-biz="{bk}" data-t="{code}"></div></div></figure>'
        secs += f'<section class="bizsec"><h2>{t["key"]} · {reg["name"]}</h2><div class="sub">기본 템플릿 상태 = {t["owner"]} 입력 없음. 상단 AI 요약 + 위생 정보 카드는 세 유형 공통, 그 아래만 다릅니다. 상호·수치는 시안용 예시.</div>{opts_table(bk)}<div class="row3">{figs}</div></section>'
    doc = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>위쳌 기본 템플릿 — 치킨집·산후조리원 × 3유형 한눈에 (10/28)</title>{B.FONT}<style>{B.CSS}{T.EXTRA_CSS}{CSS}</style></head>
<body>
<div class="top"><div class="desc"><h1>위쳌 사업장 상세 — 기본 템플릿 × 3유형, 치킨집·산후조리원 한눈에</h1>
<p>클릭 없이 보는 판입니다. 업종마다 <b>사장님 선택 항목 10개(기본 문안·질문 포함)</b>를 먼저 두고, 그 아래 같은 데이터로 만든 <b>수치형 · 인터뷰형 · 상세페이지형</b> 손님 화면을 나란히 놓았습니다. 맨 왼쪽이 <b>사장님 선택 화면</b>입니다. 처음엔 기본 선택 3개만 켜진 상태이고, 거기서 체크를 바꾸거나 글을 고치면 오른쪽 화면 3개가 같이 바뀝니다.</p></div></div>
{secs}
<script>{T.js_block()}</script>
</body></html>'''
    with open(os.path.join(OUT, FNAME), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', FNAME)

if __name__ == '__main__':
    build()
