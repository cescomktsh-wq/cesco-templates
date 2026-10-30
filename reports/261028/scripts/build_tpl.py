# -*- coding: utf-8 -*-
"""위쳌 기본 템플릿 + 사장님 선택·수정 시연 페이지 생성.
핵심: 템플릿은 이미 다 채워져 있고(업종 기본 문안), 사장님은 특장점 2~3개만 고르면 되고, 원하면 문장을 고칠 수 있다.
실행: python3 reports/261028/scripts/build_tpl.py
"""
import os, json, sys
sys.path.insert(0, os.path.dirname(__file__))
import build as B

OUT = os.path.join(os.path.dirname(__file__), '..')
FNAME = '위쳌_기본템플릿_사장님선택수정_261028.html'

# ── 업종 기본 템플릿 (등록 정보만 들어가면 완성되는 문안) ──
TPL = {
'chicken': dict(
  key='치킨집', owner='사장님', tabs=['홈','메뉴','리뷰','사진','위생'], cta='이 가게 방역 알림 받기',
  reg=dict(name='열한시 치킨', cat='치킨·닭강정', town='성수동', years='17', rating='4.7', rv='리뷰 2,041', date='10.16', report='2026-1016-0512', n=5),
  hero_lab='{town} · {years}년', hero='오늘 기름,<br>오늘 닭으로 튀겨요',
  about_h='기름과 닭과 도마를<br>매일 같은 순서로',
  about='{town}에서 {years}년째 치킨을 튀기는 {name}이에요. 기름과 닭, 도마를 매일 같은 순서로 챙겨요. 세스코가 정기 점검으로 확인한 결과를 이 페이지에 그대로 올려요.',
  strip=[('영업','등록 정보'),('메뉴','등록 정보'),('이용','등록 정보'),('주차','등록 정보')],
  pt_h='이 집이 특히<br>신경 쓰는 세 가지',
  review='리뷰에서 가장 많이 나온 말은 "바삭하다"예요. (리뷰 데이터 연결 시 자동 요약)',
  hc=B.BIZ['chicken']['hc'],
  items=[
   ('튀김 기름 교체 주기','기름은 정해진 날,<br>전부 갈아요','튀김 기름은 요일을 정해 통째로 바꿔요. 조금씩 보충하지 않아요. 새 기름으로 튀긴 날이 바삭함이 달라서, 사장님이 제일 먼저 챙기는 일이에요.','세스코 실측 · 튀김유 산가',1),
   ('생닭 당일 소진','오늘 들어온<br>닭만 써요','아침에 들어온 닭은 그날 다 써요. 남으면 다음 날로 넘기지 않아요. 가끔 일찍 닫는 날이 있는 건 그래서예요.','세스코 실측 · 생닭 냉장 온도',1),
   ('염지·숙성 시간','염지는<br>시간을 지켜요','들어온 닭은 바로 염지해서 냉장고에 둬요. 정해진 시간을 채운 닭만 튀겨요. 간이 속까지 배고 살이 촉촉한 이유예요.','세스코 실측 · 냉장 보관 온도',1),
   ('도마·칼 색 구분','생닭 도마는<br>따로 있어요','생닭 손질용 도마와 칼은 색으로 나눠 두고 다른 데 쓰지 않아요. 직원이 바뀌어도 헷갈리지 않게요.','세스코 실측 · 칼·도마 ATP',1),
   ('두 번 튀김·조리 온도','온도계 보고<br>두 번 튀겨요','튀김기 온도를 온도계로 확인하고 두 번 튀겨요. 시간이 더 걸리지만 식어도 바삭한 게 이것 때문이에요.','매장 기록',0),
   ('후드·덕트 청소 주기','후드 안쪽까지<br>닦아요','보이는 겉면만이 아니라 후드 안쪽과 덕트를 정기적으로 청소해요. 기름때가 쌓이지 않아야 주방 공기와 안전이 지켜져요.','세스코 실측 · 주방 공기',1),
   ('포장 방식','포장은<br>눅눅해지지 않게','포장 상자에 김이 빠지도록 구멍을 내고 바로 닫지 않아요. 집에 가져가서 먹어도 바삭하라고요.','매장 기록',0),
   ('닭 호수·원산지 표시','닭은 호수와 원산지를<br>적어 둬요','어떤 닭을 쓰는지 메뉴판과 매장에 적어 둬요. 손님이 물어보기 전에 먼저요.','매장 기록',0),
   ('홀 테이블·소스통 관리','테이블과 소스통은<br>손님마다','손님이 나가면 테이블을 두 번 닦고 소스통과 양념 그릇도 새로 채워요. 쓰던 걸 다음 손님에게 내지 않아요.','매장 기록',0),
   ('배달 용기·위생 장갑','배달도 매장과<br>같은 손으로','조리할 땐 장갑을 끼고 배달 용기는 밀봉해서 나가요. 배달이라고 다르게 하지 않아요.','매장 기록',0)],
  default_sel=[0,1,3],
  edit=dict(about='성수동 골목에서 17년, 아버지가 열고 아들이 잇는 집이에요. 테이블 네 개, 손님 열에 일곱은 포장. 벽 메뉴판은 손글씨고 가격은 3년째 그대로예요.',
            pts={0:'문은 열한 시에 여는데 저는 네 시 반에 나와요. 월·수·금. 알람 세 개 맞춰 놓고요. 작년에 한 번 늦잠 자서 열 시에 갈았는데 단골이 "오늘 좀 다르네" 하더라고요.'},
            say='기름은 새벽에 갈아요. 점검 오시는 날도, 안 오시는 날도요.')),
'meat': dict(
  key='고깃집', owner='사장님', tabs=['홈','메뉴','리뷰','사진','위생'], cta='이 가게 방역 알림 받기',
  reg=dict(name='일도씨 정육식당', cat='돼지고기 구이·삼겹살', town='마포', years='3', rating='4.6', rv='리뷰 1,318', date='10.14', report='2026-1014-0287', n=5),
  hero_lab='{town} · {years}년', hero='고기는<br>온도로 관리해요',
  about_h='고기는 온도로, 불판은 손님마다,<br>반찬은 당일로',
  about='{town}에서 {years}년째 고기를 굽는 {name}이에요. 고기는 온도로, 불판은 손님마다, 반찬은 당일로 관리해요. 세스코가 정기 점검으로 확인한 결과를 이 페이지에 그대로 올려요.',
  strip=[('영업','등록 정보'),('메뉴','등록 정보'),('이용','등록 정보'),('주차','등록 정보')],
  pt_h='이 집이 특히<br>신경 쓰는 세 가지',
  review='리뷰에서 가장 많이 나온 말은 "불판을 자주 바꿔 준다"예요. (리뷰 데이터 연결 시 자동 요약)',
  hc=B.BIZ['meat']['hc'],
  items=[
   ('숙성고 온도·숙성 일수','고기는<br>온도로 관리해요','숙성고 온도를 정해 두고 하루에도 몇 번씩 확인해요. 입고일을 적어 두고 정해진 날이 지난 고기는 내지 않아요.','세스코 실측 · 숙성고 온도',1),
   ('입고 검수','고기는 사장님이<br>직접 받아요','들어오는 고기는 상자를 열어 색과 온도를 확인하고 받아요. 기준에 안 맞으면 돌려보내요.','매장 기록',0),
   ('불판 교체 기준','불판은<br>손님마다 새것','불판은 손님마다 새것으로 내고, 타기 시작하면 바로 바꿔 드려요. 닦아 둔 불판을 따로 쌓아 둬요.','세스코 실측 · 세척 불판 ATP',1),
   ('집게·가위 분리','생고기 집게는<br>따로 있어요','생고기용 집게와 익은 고기용 집게를 색으로 나눠요. 처음 오신 분께는 직원이 먼저 알려드려요.','세스코 실측 · 집게·가위 ATP',1),
   ('남은 반찬 폐기·소분 냉장','남은 반찬은<br>다시 안 내요','테이블에서 남은 반찬은 그 자리에서 버려요. 반찬은 소분해서 냉장에 두고 당일 것만 나가요.','세스코 확인 · 반찬 소분 냉장',1),
   ('숯·화덕 관리','숯은<br>때맞춰 갈아요','숯이 약해지면 바로 바꿔 드려요. 불판 바꿀 때 숯도 같이 봐요.','매장 기록',0),
   ('테이블 후드·연기','연기는 테이블에서<br>바로 빼요','테이블마다 후드가 있어 연기가 홀에 머물지 않아요. 옷에 냄새가 덜 배는 이유예요.','세스코 실측 · 홀 공기',1),
   ('등급판정서·원산지 게시','오늘 고기의<br>등급판정서가 있어요','축산물 등급판정서와 원산지를 매장에 붙여 둬요. 어디서 온 고기인지 보고 드실 수 있어요.','세스코 확인 · 등급판정서',1),
   ('직접 담근 재료','된장·김치는<br>직접 담가요','찌개 된장과 김치는 직접 담근 걸 써요. 사 오는 것보다 손이 많이 가지만 맛이 달라서요.','매장 기록',0),
   ('홀 환기·공기청정기','홀 공기도<br>관리해요','공기청정기를 영업 내내 켜 두고 환기 시간을 정해 둬요. 고기 연기 속 미세먼지까지 신경 써요.','세스코 실측 · 홀 공기',1)],
  default_sel=[0,2,4],
  edit=dict(about='마포 골목 안쪽, 테이블 여섯 개. 정육점 9년 하다 연 지 3년이에요. 상호의 \'일도\'는 숙성고 온도. 단골들이 붙인 별명이 그대로 간판이 됐어요.',
            pts={0:'제 폰 잠금화면이 숙성고 온도예요. 2년 전에 정전으로 4도까지 올라간 적이 있어서 그날 고기 다 뺐어요. 그 뒤로 센서 달고 알림 오게 했어요. 사흘 넘긴 고기는 안 냅니다.', 2:'한 테이블에 세 번 바꿀 때도 있어요. 불판만 닦으시는 분이 두 시에 오세요. 오셔서 제일 먼저 불판을 세요. 마흔 장 아래면 저한테 문자가 와요.'},
            say='고기는 온도로 먹는 거예요. 숙성고 1도, 불판 새것, 반찬 새것.')),
'care': dict(
  key='산후조리원', owner='원장님', tabs=['홈','프로그램','리뷰','사진','위생'], cta='이 조리원 방역 알림 받기',
  reg=dict(name='볕드는집 산후조리원', cat='산후조리원 · 민간형', town='분당', years='6', rating='4.9', rv='후기 412', date='10.15', report='2026-1015-0341', n=6),
  hero_lab='{town} · 민간형', hero='아기한테 닿는<br>순서대로 봐요',
  about_h='공기, 젖병, 수유실을<br>먼저 봐요',
  about='{town}에 있는 {name}이에요. 산모와 아기가 2주를 지내는 곳이라 공기와 젖병, 수유실을 먼저 봐요. 세스코가 정기 점검으로 확인한 결과를 이 페이지에 그대로 올려요.',
  strip=[('이용','등록 정보'),('식사','등록 정보'),('면회','등록 정보'),('프로그램','등록 정보')],
  pt_h='2주를 지내는 곳이라<br>이 세 가지를 봐요',
  review='후기에서 가장 많이 나온 말은 "방이 밝다"예요. (리뷰 데이터 연결 시 자동 요약)',
  hc=B.BIZ['care']['hc'],
  items=[
   ('신생아실 공기 수치 공개','신생아실 공기 수치를<br>공개해요','신생아실 공기는 매달 세스코가 측정하고, 결과를 복도에 붙여 둬요. 숫자를 숨기지 않아요.','세스코 실측 · 신생아실 부유세균',1),
   ('젖병·수건 아기별 구분','젖병은<br>아기마다 따로','젖병과 수건은 아기마다 구분해서 쓰고 매일 고온 살균해요. 다른 아기 것과 섞이지 않아요.','세스코 실측 · 젖병 내부 ATP',1),
   ('산모 방 창·환기','산모 방은<br>창을 열어요','방마다 창이 있고 정해진 시간에 환기해요. 2주를 지내는 방이라 공기와 햇볕을 먼저 봐요.','세스코 실측 · 산모 방 부유세균',1),
   ('면회·출입 관리','면회는<br>창 너머로','신생아실은 창 너머로만 보고, 외부 방문은 시간과 인원을 정해 둬요. 폰으로 아기를 볼 수 있어요.','매장 기록',0),
   ('수유실 소독 주기','수유실은<br>시간마다 소독해요','수유실 소파와 손잡이는 정해진 간격으로 소독하고 체크표에 시간과 사인을 남겨요.','세스코 실측 · 수유실 손잡이 ATP',1),
   ('침구·세탁 동선 분리','침구는 매일,<br>세탁은 동선을 나눠요','침구는 매일 갈고 속싸개는 하루 두 번 바꿔요. 깨끗한 세탁물과 나가는 세탁물이 같은 문을 쓰지 않아요.','세스코 확인 · 세탁 동선',1),
   ('산모식 식재료·조리실','산모식은<br>조리실부터 봐요','식재료 보관 온도와 조리대를 관리하고, 미역국은 하루 두 번 새로 끓여요.','세스코 실측 · 산모식 조리대 ATP',1),
   ('좌욕기·비데 소독','좌욕기는 쓰고 나면<br>바로 소독','좌욕기와 비데는 사용 후 바로 소독해요. 순서표를 붙여 두고 그대로 해요.','세스코 실측 · 좌욕기 ATP',1),
   ('신생아실 야간 운영','밤에도 신생아실은<br>같은 인원','밤에도 간호 인력이 신생아실을 지키고 조명만 낮춰요. 밤에 폰으로 봐도 아기가 보여요.','매장 기록',0),
   ('간호 인력','신생아실은<br>간호사가 봐요','신생아실은 간호사가 상주하고 원장이 직접 돌아봐요. 궁금한 건 바로 물어볼 수 있어요.','매장 기록',0)],
  default_sel=[0,1,2],
  edit=dict(about='분당, 방 열두 개짜리 민간 조리원이에요. 원장은 신생아실 간호사 12년. 매달 세스코가 재면 신생아실 공기 수치를 새 종이에 손으로 써서 복도에 붙여요.',
            pts={0:'지난달 숫자 위에 덧쓰지 않고 새 종이로 바꿔요. 숫자는 세스코가 재고 저는 옮겨 적기만 해요. 제가 쓰면 그건 광고잖아요.'},
            say='숫자는 세스코가 재요. 저는 복도에 붙이기만 해요.')),
}

# 인터뷰형 질문(셀프 인터뷰) · 수치형 매핑(위생 카드 실측 항목 index, 없으면 -1)
QS = {
'chicken': ['기름은 언제 갈아요?','닭은 언제 들어오고 언제까지 써요?','염지는 어떻게 해요?','생닭 손질할 때 도마는요?','두 번 튀기는 이유가 있어요?','후드 청소는 누가, 얼마나 자주 해요?','포장하면 눅눅해지지 않나요?','어떤 닭을 쓰세요?','테이블이랑 소스통은요?','배달은 매장이랑 다른 게 있어요?'],
'meat': ['고기는 몇 도에 두세요?','고기 들어올 때 뭘 보세요?','불판은 언제 바꿔 줘요?','집게가 두 개 나오던데요?','남은 반찬은 어떻게 해요?','숯은 언제 갈아요?','연기는 어떻게 빼요?','오늘 고기는 어디서 온 거예요?','된장이랑 김치는 직접 담그세요?','홀 공기는 어떻게 관리해요?'],
'care': ['신생아실 공기는 어떻게 확인해요?','젖병은 아기마다 따로 써요?','산모 방 환기는요?','면회는 어떻게 해요?','수유실 소독은 얼마나 자주 해요?','침구랑 세탁은요?','산모식은 누가 어떻게 만들어요?','좌욕기는 쓰고 나면요?','밤에는 신생아실에 누가 있어요?','신생아실은 누가 봐요?'],
}
MET = {
'chicken': [0,1,1,2,-1,3,-1,-1,-1,-1],
'meat':    [0,-1,1,2,-1,-1,3,-1,-1,3],
'care':    [0,1,-1,-1,2,-1,3,-1,-1,-1],
}

# JS로 넘길 데이터
DATA = {}
for k, t in TPL.items():
    d = dict(t); d['place'] = '조리원' if k=='care' else '가게'; d['items'] = [dict(label=a, title=b, copy=c, chip=e, cesco=f, q=QS[k][i], metric=MET[k][i]) for i, (a, b, c, e, f) in enumerate(t['items'])]
    hc = t['hc']; d['hc'] = dict(pill=hc['pill'], hl=hc['hl'], ds=hc['ds'], sum=hc['sum'], metrics=[dict(k=m[0], v=m[1], u=m[2], pct=m[3], base=m[4]) for m in hc['metrics']])
    DATA[k] = d

EXTRA_CSS = r"""
.top{max-width:1320px;margin:0 auto;padding:20px 20px 0}
.two-col{display:flex;gap:28px;justify-content:center;align-items:flex-start;flex-wrap:wrap;max-width:1320px;margin:0 auto;padding:0 20px 60px}
.col{width:390px;flex-shrink:0}
.col h3{margin:0 0 8px 4px;font-size:12.5px;font-weight:800;color:var(--ink)}
.col h3 small{display:block;font-weight:500;color:var(--muted);font-size:11.5px}
/* 사장님 편집 화면 */
.ed{background:#fff;border-radius:28px;box-shadow:0 10px 30px rgba(0,0,0,.14),0 0 0 1px rgba(0,0,0,.06);overflow:hidden}
.ed .bar{height:52px;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:800;color:var(--ink);border-bottom:1px solid var(--line);position:relative}
.ed .bar .sv{position:absolute;right:12px;top:12px;height:28px;padding:0 12px;border-radius:8px;background:var(--wc);color:#fff;font-size:12px;font-weight:800;display:flex;align-items:center}
.ed .in{padding:14px 16px 18px;display:flex;flex-direction:column;gap:14px}
.ed .seg{display:flex;gap:6px}
.ed .seg button{flex:1;font:inherit;font-size:12px;font-weight:800;padding:8px 0;border-radius:10px;border:1px solid #D9DCD6;background:#fff;color:var(--ink);cursor:pointer}
.ed .seg button.on{background:var(--wc);border-color:var(--wc);color:#fff}
.ed .fs{border:0;padding:0;margin:0}
.ed .lb{display:flex;align-items:baseline;gap:6px;font-size:12.5px;font-weight:900;color:var(--ink);margin-bottom:6px}
.ed .lb small{font-weight:600;color:var(--muted);font-size:10.5px;margin-left:auto}
.ed .lock{font-size:11px;color:var(--muted);background:#F2F4F7;border-radius:10px;padding:9px 11px;line-height:1.5}
.ed .lock b{color:var(--ink2)}
.ed .chk{display:flex;flex-direction:column;gap:5px}
.ed .chk label{display:grid;grid-template-columns:18px 1fr auto;gap:8px;align-items:center;padding:8px 10px;border:1px solid #E3E6E1;border-radius:10px;font-size:12.5px;font-weight:700;color:var(--ink);cursor:pointer}
.ed .chk label.on{border-color:var(--wc);background:var(--wc-bg)}
.ed .chk label.dis{opacity:.45}
.ed .chk input{margin:0;width:16px;height:16px;accent-color:var(--wc)}
.ed .chk .ord{font-size:9.5px;font-weight:900;color:#fff;background:var(--wc);border-radius:999px;padding:1px 7px;visibility:hidden}
.ed .chk label.on .ord{visibility:visible}
.ed .chk .cs{font-size:9.5px;font-weight:800;color:var(--wc);margin-left:6px}
.ed .chk .cs.o{color:var(--muted)}
.ed textarea,.ed input[type=text]{width:100%;font:inherit;font-size:12.5px;line-height:1.5;color:var(--ink2);border:1px solid #D9DCD6;border-radius:10px;padding:9px 10px;resize:vertical;background:#fff}
.ed textarea:focus,.ed input:focus{outline:2px solid var(--wc);border-color:var(--wc)}
.ed textarea.changed,.ed input.changed{background:var(--amber-bg);border-color:#F0C27A}
.ed .cnt{font-size:10px;color:var(--muted);text-align:right;margin-top:2px}
.ed .pt-ed{border:1px solid #E3E6E1;border-radius:12px;padding:10px;margin-top:8px}
.ed .pt-ed .t{font-size:11.5px;font-weight:900;color:var(--wc);margin-bottom:5px}
.ed .pt-ed .t span{color:var(--ink);margin-left:6px}
.ed .pt-ed .ph{height:52px;margin-top:6px;font-size:10px}
.ed .btns{display:flex;gap:6px}
.ed .btns button{flex:1;font:inherit;font-size:11.5px;font-weight:800;padding:8px 0;border-radius:10px;border:1px solid #D9DCD6;background:#fff;color:var(--ink);cursor:pointer}
.ed .btns button.ex{border-color:var(--amber);color:var(--amber);background:var(--amber-bg)}
.tsel{display:flex;gap:6px;margin:0 0 10px}
.tsel button{flex:1;font:inherit;font-size:12px;font-weight:800;padding:8px 0;border-radius:10px;border:1px solid #D9DCD6;background:#fff;color:var(--ink);cursor:pointer}
.tsel button.on{background:var(--ink);border-color:var(--ink);color:#fff}
.ed .pt-ed .qq{font-size:10.5px;color:var(--muted);margin:-2px 0 6px}
.ed .note{font-size:10.5px;color:var(--muted);line-height:1.5}
/* 손님 화면 쪽 수정 표시 */
mark.ed{background:var(--amber-bg);color:inherit;box-shadow:0 0 0 2px var(--amber-bg);border-radius:2px}
.dp .say2{margin:0 24px 28px;background:#FFF8E8;border:1px solid #F3E2B8;border-radius:12px;padding:12px 14px;text-align:left}
.dp .say2 .lb{font-size:9.5px;letter-spacing:.1em;color:#9A6B12}
.dp .say2 p{font-size:13px;color:#111;font-weight:600;line-height:1.6;margin-top:4px}
.dp .say2 small{font-size:10.5px;color:#8A8A8A}
.dp .pt .pho{height:200px}
.dp .hr{height:300px}
.memo{max-width:1240px;margin:0 auto 40px;background:#fff;border-radius:12px;padding:16px 18px;font-size:12.5px;color:#3E444A;line-height:1.6}
.memo h2{margin:0 0 8px;font-size:15px;font-weight:900;color:var(--ink)}
.memo .tw{overflow-x:auto;margin-top:8px}
.memo table{width:100%;min-width:640px;border-collapse:collapse;font-size:12px}
.memo th,.memo td{border:1px solid var(--line);padding:7px 9px;vertical-align:top;text-align:left;line-height:1.5}
.memo th{background:#F6F7F4;font-weight:800;color:var(--ink);white-space:nowrap}
.memo .flag{display:inline-block;background:var(--amber-bg);color:var(--amber);font-weight:800;border-radius:3px;padding:0 5px;font-size:10.5px;margin-right:3px}
@media (max-width:760px){.top{padding:12px 0 0}.two-col{padding:0 0 40px;gap:16px}.col{width:100%}.ed{border-radius:0;box-shadow:none}.col h3{padding:0 16px}.memo{border-radius:0}}
"""

JS = r"""
const D = __DATA__;
const CHK = '__CHK__';
let cur = (location.hash.slice(1) in D) ? location.hash.slice(1) : 'chicken';
let typ = 'C';
const state = {};   // per biz: {sel:[...], about, pts:{i:copy}, say, example:false}
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;');}
function fill(s, reg){return s.replace(/\{(\w+)\}/g,(m,k)=>reg[k]||m);}
function init(bk){const t=D[bk]; state[bk]={sel:[...t.default_sel], about:fill(t.about,t.reg), pts:{}, say:'', example:false}; t.items.forEach((it,i)=>state[bk].pts[i]=it.copy);}
Object.keys(D).forEach(init);
window.addEventListener('hashchange',()=>{const k=location.hash.slice(1); if(k in D){cur=k;render();}});
function mark(txt, base){ return txt!==base ? '<mark class="ed">'+esc(txt)+'</mark>' : esc(txt); }

function editorHtml(bk, s, withBiz){
  const t=D[bk], reg=t.reg;
  let h='';
  if(withBiz) h+='<div class="fs"><div class="lb">업종<small>등록 정보로 자동 선택</small></div><div class="seg">'+['chicken','care'].map(k=>`<button type="button" data-biz="${k}" class="${k===bk?'on':''}">${D[k].key}</button>`).join('')+'</div></div>';
  h+=`<div class="lock"><b>세스코가 입력 · ${t.owner}은 수정 불가</b><br>위생 등급 A · 점검일 ${reg.date} · 실측 ${reg.n}항목 · 리포트 No. ${reg.report}<br><b>등록 정보에서 자동</b> ${reg.name} · ${reg.cat} · ${reg.town} · ${reg.years}년 · 영업시간 · 메뉴 · 주차</div>`;
  h+=`<div class="fs"><div class="lb">① 우리 ${t.place}가 특히 신경 쓰는 것<small>2~3개 선택 · 고른 순서대로 노출</small></div><div class="chk">`;
  t.items.forEach((it,i)=>{const on=s.sel.includes(i); const dis=!on&&s.sel.length>=3;
    h+=`<label class="${on?'on':''}${dis?' dis':''}"><input type="checkbox" data-i="${i}" ${on?'checked':''} ${dis?'disabled':''}><span>${it.label}<span class="cs ${it.cesco?'':'o'}">${it.cesco?'세스코 점검 항목':'매장 기록'}</span></span><span class="ord">${on?(s.sel.indexOf(i)+1):''}</span></label>`;});
  h+='</div></div>';
  h+=`<div class="fs"><div class="lb">② ${t.place} 소개<small>기본 문안이 들어 있어요 · 160자</small></div><textarea data-f="about" rows="4" class="${s.about!==fill(t.about,reg)?'changed':''}">${esc(s.about)}</textarea><div class="cnt">${s.about.length}/160</div></div>`;
  h+='<div class="fs"><div class="lb">③ 고른 항목의 설명<small>그대로 둬도 돼요 · 각 140자</small></div>';
  s.sel.forEach((i,n)=>{const it=t.items[i]; h+=`<div class="pt-ed"><div class="t">POINT 0${n+1}<span>${it.title.replace('<br>',' ')}</span></div><div class="qq">인터뷰형에선 이 질문의 답으로 나가요: “${it.q}”</div><textarea data-pt="${i}" rows="3" class="${s.pts[i]!==it.copy?'changed':''}">${esc(s.pts[i])}</textarea><div class="cnt">${s.pts[i].length}/140</div><div class="ph">사진 추가 (선택) · 없으면 점검 때 촬영한 사진</div></div>`;});
  h+='</div>';
  h+=`<div class="fs"><div class="lb">④ ${t.owner} 한마디<small>선택 · 40자</small></div><input type="text" data-f="say" value="${esc(s.say)}" placeholder="비워 두면 이 칸은 손님 화면에 안 나와요" class="${s.say?'changed':''}"><div class="cnt">${s.say.length}/40</div></div>`;
  h+='<div class="btns"><button type="button" data-act="reset">기본 문안으로 되돌리기</button><button type="button" class="ex" data-act="example">${t.owner}이 고친 예시 넣기</button></div>';
  h+='<div class="note">저장하면 손님 화면에 바로 반영돼요. 세스코 측정값·등급·점검일은 ${t.owner}이 바꿀 수 없어요. 주황색 칸이 ${t.owner}이 고친 곳이에요.</div>';
  return h;
}

function previewHtml(bk, typ, s){
  const t=D[bk], reg=t.reg, hc=t.hc;
  const tabs=t.tabs.map(x=>`<span class="${x==='위생'?'on':''}">${x}</span>`).join('');
  const ai=[ `세스코가 ${reg.date}에 ${reg.n}가지를 직접 재서 모두 기준 안이었어요.`, `${t.owner}이 고른 관리 포인트: ${s.sel.map(i=>t.items[i].label).join(', ')}`, t.review ].map(x=>`<li>${x}</li>`).join('');
  const ms=hc.metrics.map(m=>`<div class="m"><div class="k">${m.k}<i>적합</i></div><div class="v">${m.v}${m.u?' <small>'+m.u+'</small>':''}</div><div class="bar"><i style="width:${m.pct}%"></i></div><div class="b">${m.base}</div></div>`).join('');
  const strip=t.strip.map(x=>`<div><b>${x[0]}</b><span>${x[1]}</span></div>`).join('');
  const pts=s.sel.map((i,n)=>{const it=t.items[i]; return `<div class="pt${n%2?' alt':''}"><div class="pho">사진 자리 · ${it.label}</div><div class="tx"><div class="num">POINT 0${n+1}</div><h3>${it.title}</h3><p>${mark(s.pts[i],it.copy)}</p><div class="fx"><i>${CHK}</i>${it.chip}</div></div></div>`;}).join('');
  const say = s.say ? `<div class="say2"><div class="lb">${t.owner} 한마디</div><p><mark class="ed">"${esc(s.say)}"</mark></p><small>${reg.name} ${t.owner}</small></div>` : '';
  const headHtml=`
<div class="appbar"><button class="back" aria-label="뒤로 가기"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1A1A1A" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg></button><div class="t">${reg.name}</div></div>
<div class="head"><div class="nm"><h2>${reg.name}</h2><span class="cat">${reg.cat}</span></div><div class="rv"><svg width="13" height="13" viewBox="0 0 24 24" fill="#C77700"><path d="M12 2l2.9 6.2 6.6.8-4.9 4.6 1.3 6.5L12 16.8 6.1 20l1.3-6.5L2.5 9l6.6-.8z"/></svg><b>${reg.rating}</b><span>${reg.rv} · ${reg.town}</span></div><div class="tabs">${tabs}</div></div>
<div class="body" style="padding-bottom:12px">
<div class="ai"><div class="lb">AI 요약<small>세스코 리포트 · 사장님 선택 · 리뷰</small></div><ul>${ai}</ul></div>
<div class="hc"><div class="top"><div class="grade"><b>A</b><span>위생 등급</span></div><div class="t"><b>세스코 전문가 실측 · ${reg.date} · ${reg.n}가지 모두 기준 안</b><span>위생점검 리포트 No. ${reg.report} · 다음 점검 11월</span></div></div><div class="pt"><span class="pill">${hc.pill}</span><small>CESCO 위쳌 기준</small><div class="hl">${hc.hl}</div><div class="ds">${hc.ds}</div></div>${typ==='A'?'<div class="grid">'+ms+'</div>':''}<div class="sum"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0072CE" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg><div>${hc.sum}</div></div></div>`;
  const bodyC=`<div class="dp">
<div class="hr"><div class="pho">사진 자리 · 대표 세로 컷 (사장님 또는 점검 촬영)</div><div class="ov"><span class="lab">${fill(t.hero_lab,reg)}</span><h1>${t.hero}</h1><div class="sub">${reg.name} · 세스코 위생 실측 A</div></div></div>
<div class="sec"><span class="lab">ABOUT</span><h2>${t.about_h}</h2><p>${mark(s.about, fill(t.about,reg))}</p><div class="strip">${strip}</div></div>
<div class="sec alt" style="padding-bottom:10px"><span class="lab">POINT</span><h2>${t.pt_h}</h2></div>
${pts}
${say}
<div style="height:8px"></div>
<div class="rep"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1A3668" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg><div class="t">위생점검 리포트 No. ${reg.report}<small>세스코 전문가 현장 측정·서명 원본</small></div><a class="btn sec" href="#">원본 보기</a></div>
<p class="fine2">측정값은 점검일 기준이며 다음 정기 점검 시 갱신돼요. POINT는 ${t.owner}이 고른 항목이고, "세스코 실측·확인" 표시가 있는 것만 점검에서 실제로 봤어요.</p>
</div>`;
  const repRow=`<div class="report"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1A3668" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg><div class="t">위생점검 리포트 No. ${reg.report}<small>세스코 전문가 현장 측정·서명 원본</small></div><a class="btn sec" href="#">원본 보기</a></div>`;
  const fine=`<p class="fine">측정값은 점검일 기준이며 다음 정기 점검 시 갱신돼요. 관리 포인트는 ${t.owner}이 고른 항목이고, "세스코 실측·확인" 표시가 있는 것만 점검에서 실제로 봤어요.</p>`;
  const sayCard = s.say ? `<div class="card say"><div class="lb">${t.owner} 한마디</div><p><mark class="ed">"${esc(s.say)}"</mark></p><div class="sg">${reg.name} ${t.owner}</div></div>` : '';
  // A · 수치형
  const gauges=hc.metrics.map((m,mi)=>{
    const sel=s.sel.filter(i=>t.items[i].metric===mi);
    const why=sel.map(i=>`<div class="why1"><b>이 집은</b> ${mark(s.pts[i],t.items[i].copy)}</div>`).join('');
    return `<div class="r"><div class="k">${m.k}</div><div class="mt" style="margin-top:3px"><div class="mrow"><b>${m.v}</b>${m.u?'<small>'+m.u+'</small>':''}<span class="pill2">기준의 ${m.pct}%</span></div><div class="mb"><i style="width:${m.pct}%"></i></div><div class="ml"><span>0</span><span>${m.base}</span></div></div>${why}</div>`;}).join('');
  const rest=s.sel.filter(i=>t.items[i].metric<0);
  const restList = rest.length ? `<div class="card list"><div class="hd"><b>실측 항목 밖에서 ${t.owner}이 고른 것</b><span>매장 기록</span></div>${rest.map(i=>`<div class="row"><span style="width:8px;height:8px;border-radius:50%;background:#C9D0D8;display:block;margin:0 auto"></span><div class="k">${t.items[i].title.replace('<br>',' ')}<small>${mark(s.pts[i],t.items[i].copy)}</small></div><span class="tag o">매장 기록</span></div>`).join('')}</div>` : '';
  const bodyA=`<div class="body">
<div class="card intro"><div class="byline"><div class="av"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0072CE" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/></svg></div><div><b>${reg.name}은요</b><span>${t.owner}이 적은 소개</span></div></div><p style="margin-top:8px">${mark(s.about, fill(t.about,reg))}</p></div>
<div class="sh2"><b>항목별로 얼마나 여유 있나</b><small>${reg.date} 세스코 실측 · 값과 기준선</small></div>
<div class="res">${gauges}</div>
${restList}
${sayCard}
${repRow}${fine}</div>`;
  // B · 인터뷰형 (셀프 인터뷰)
  const qa=s.sel.map(i=>{const it=t.items[i]; return `<div class="it"><div class="q">${it.q}</div><div class="a">${mark(s.pts[i],it.copy)}</div><div class="fact"><i>${CHK}</i>${it.chip}</div></div>`;}).join('');
  const pull = s.say ? `<div class="pull"><p><mark class="ed" style="background:transparent;box-shadow:none">"${esc(s.say)}"</mark></p><span>${reg.name} ${t.owner}</span></div>` : '';
  const bodyB=`<div class="body">
<div class="iv-hero"><div class="ph">사진 자리 · ${t.owner} · 대표 컷 (${t.owner} 업로드 또는 점검 촬영)</div><div class="eb">${t.owner} 셀프 인터뷰 · ${reg.date} 점검 후</div><h3>${t.about_h}</h3><div class="who">${reg.name} · 질문은 위쳌이, 답은 ${t.owner}이 직접 적었어요</div></div>
<div class="card intro"><p>${mark(s.about, fill(t.about,reg))}</p></div>
<div class="card iv">${qa}</div>
${pull}
${repRow}${fine}</div>`;
  const body = typ==='A'?bodyA : typ==='B'?bodyB : bodyC;
  return headHtml + body + `<div class="actions"><div class="ico">전화</div><div class="ico">저장</div><div class="cta">${t.cta}</div></div>`;
}
function refreshPreviews(bk){
  document.querySelectorAll('[data-static]').forEach(el=>{ if(el.dataset.biz===bk) el.innerHTML=previewHtml(bk, el.dataset.t, state[bk]); });
}
function refresh(bk){
  document.querySelectorAll('[data-ed]').forEach(el=>{ if(el.dataset.biz===bk) el.innerHTML=editorHtml(bk, state[bk], el.hasAttribute('data-withbiz')); });
  refreshPreviews(bk);
}
const edIn=document.getElementById('ed-in'), pv=document.getElementById('pv');
function render(){
  if(edIn){ edIn.dataset.biz=cur; pv.dataset.biz=cur; pv.dataset.t=typ; document.querySelectorAll('.tsel button').forEach(b=>b.classList.toggle('on',b.dataset.t===typ)); }
  Object.keys(D).forEach(refresh);
}
document.addEventListener('click',e=>{
  const tb=e.target.closest('.tsel button[data-t]'); if(tb){typ=tb.dataset.t; render(); return;}
  const ed=e.target.closest('[data-ed]'); if(!ed) return; const bk=ed.dataset.biz;
  const b=e.target.closest('button[data-biz]'); if(b){cur=b.dataset.biz;history.replaceState(null,'','#'+cur);render();return;}
  const a=e.target.closest('button[data-act]'); if(!a) return;
  const t=D[bk]; if(a.dataset.act==='reset'){init(bk);} else {const s=state[bk]; s.about=t.edit.about; Object.entries(t.edit.pts).forEach(([i,c])=>{i=+i; if(!s.sel.includes(i)) s.sel=[i,...s.sel].slice(0,3); s.pts[i]=c;}); s.say=t.edit.say;}
  refresh(bk);
});
document.addEventListener('change',e=>{
  const ed=e.target.closest('[data-ed]'); if(!ed) return; const bk=ed.dataset.biz;
  const c=e.target; if(c.type!=='checkbox') return; const s=state[bk], i=+c.dataset.i;
  if(c.checked){ if(!s.sel.includes(i)&&s.sel.length<3) s.sel.push(i);} else s.sel=s.sel.filter(x=>x!==i);
  refresh(bk);
});
document.addEventListener('input',e=>{
  const ed=e.target.closest('[data-ed]'); if(!ed) return; const bk=ed.dataset.biz;
  const el=e.target, s=state[bk];
  if(el.dataset.f==='about') s.about=el.value.slice(0,160);
  else if(el.dataset.f==='say') s.say=el.value.slice(0,40);
  else if(el.dataset.pt!==undefined) s.pts[+el.dataset.pt]=el.value.slice(0,140);
  else return;
  const t=D[bk]; el.classList.toggle('changed', el.dataset.f==='about'? s.about!==fill(t.about,t.reg) : el.dataset.f==='say'? !!s.say : s.pts[+el.dataset.pt]!==t.items[+el.dataset.pt].copy);
  el.parentElement.querySelector('.cnt').textContent=el.value.length+'/'+(el.dataset.f==='about'?160:el.dataset.f==='say'?40:140);
  refreshPreviews(bk);
});
render();
"""

def js_block():
    return JS.replace('__DATA__', json.dumps(DATA, ensure_ascii=False)).replace('__CHK__', B.CHK.replace("'", "\\'"))

def build():
    rows = ''
    for k, t in TPL.items():
        if k == 'meat': continue
        for i, (a, b, c, e, f) in enumerate(t['items'], 1):
            rows += f'<tr><td>{t["key"]}</td><td>{i}</td><td>{a}</td><td>{b.replace("<br>"," ")}</td><td>{c}</td><td>{e}</td></tr>'
    doc = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>위쳌 기본 템플릿 + 사장님 선택·수정 (10/28)</title>{B.FONT}<style>{B.CSS}{EXTRA_CSS}</style></head>
<body>
<div class="top"><div class="desc"><h1>위쳌 사업장 상세 — 기본 템플릿은 이미 채워져 있고, 사장님은 2~3개만 고르고, 원하면 고친다</h1>
<p>왼쪽은 <b>사장님 편집 화면</b>, 오른쪽은 <b>손님이 보는 화면</b>입니다. 업종을 고르면 기본 문안이 다 들어간 페이지가 바로 나오고(0 입력 상태), 특장점을 체크하면 그 순서대로 POINT가 바뀌고, 입력칸의 글을 고치면 오른쪽에 바로 반영됩니다. 고친 곳은 주황색으로 보입니다(검토용). "사장님이 고친 예시 넣기"를 누르면 실제 사장님이 손본 상태가 어떻게 달라지는지 볼 수 있습니다. 세스코 측정값·등급·점검일·등록 정보는 사장님이 못 건드립니다.</p></div></div>
<div class="two-col">
<div class="col"><h3>사장님 편집 화면<small>위쳌 사업주용 · 기본 문안이 미리 들어 있음</small></h3><div class="ed"><div class="bar">위생 페이지 관리<span class="sv">저장</span></div><div class="in" id="ed-in" data-ed data-withbiz data-biz="chicken"></div></div></div>
<div class="col"><h3>손님이 보는 화면<small>같은 데이터로 유형만 바꿔 봅니다 · 편집 즉시 반영</small></h3><div class="tsel"><button type="button" data-t="A">수치형</button><button type="button" data-t="B">인터뷰형</button><button type="button" data-t="C" class="on">상세페이지형</button></div><div class="phone"><div class="fold"><span>첫 화면 끝</span></div><div id="pv" data-static data-biz="chicken" data-t="C"></div></div></div>
</div>
<div class="memo"><h2>구조 메모</h2>
<div class="tw"><table><thead><tr><th style="width:18%">단계</th><th style="width:32%">누가 무엇을</th><th>화면에 나오는 것</th></tr></thead><tbody>
<tr><td><b>0 · 기본 제공</b></td><td>세스코 점검 데이터 + 등록 정보만 있음. 사장님 입력 없음</td><td>업종 기본 소개 문구, 업종 기본 특장점 3개(기본 선택), 기본 문안 그대로. 이 상태로도 완성된 페이지</td></tr>
<tr><td><b>1 · 고르기</b></td><td>사장님이 특장점 10개 중 2~3개 체크 (고른 순서 = 노출 순서)</td><td>POINT 01~03이 고른 항목의 기본 문안으로 바뀜. AI 요약 두 번째 줄도 같이 바뀜</td></tr>
<tr><td><b>2 · 고치기</b></td><td>사장님이 소개(160자)·항목 설명(140자)·한마디(40자)를 고침. 사진 추가</td><td>고친 문장만 바뀜. 안 고친 칸은 기본 문안 유지. 한마디는 적었을 때만 나옴</td></tr>
<tr><td><b>유형 (세스코가 정함)</b></td><td>수치형 · 인터뷰형 · 상세페이지형. 사장님 입력은 세 유형 공통</td><td>수치형: 실측 계기판 아래 "이 집은 ~"로 사장님 문장이 붙음. 인터뷰형: 고른 항목이 질문이 되고 사장님 문장이 답이 됨(셀프 인터뷰). 상세페이지형: POINT 01~03</td></tr>
<tr><td><b>세스코 전용</b></td><td>측정값·등급·점검일·리포트·"세스코 확인" 칩</td><td>사장님이 못 바꿈. 사장님이 고른 항목이라도 점검 항목이 아니면 POINT 아래 칩이 "매장 기록"으로만 표시</td></tr>
</tbody></table></div>
<p style="margin-top:10px"><span class="flag">확인 필요</span>글자 수 상한(160·140·40), 사진 장수, 사장님 수정분의 검수 여부(자동 게시 vs 세스코 승인 후 게시), 금지어 필터(가이드라인 표기법 ⑭⑮) 적용 위치.</p>
<h2 style="margin-top:18px">업종별 기본 문안 20개 (치킨집·산후조리원 특장점 선택 항목)</h2>
<p>각 항목은 제목 2줄 + 설명 2~3문장 + 세스코 확인 칩 조건으로 한 벌입니다. 수치·법령·효능 표현은 넣지 않았고, 매장이 하는 "행동"만 적었습니다. 사장님은 설명 문장만 고칠 수 있고 제목과 칩은 고정입니다.</p>
<div class="tw"><table><thead><tr><th>업종</th><th>#</th><th>선택 항목</th><th>제목(고정)</th><th>기본 설명(사장님 수정 가능)</th><th>칩</th></tr></thead><tbody>{rows}</tbody></table></div>
</div>
<script>{js_block()}</script>
</body></html>'''
    with open(os.path.join(OUT, FNAME), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', FNAME)

if __name__ == '__main__':
    build()
