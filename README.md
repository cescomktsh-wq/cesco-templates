# 세스코 콘텐츠 템플릿 (마스터)

세스코 채널별 콘텐츠 템플릿 정본. 채널 16개·유형 35종(문서 55건)을 단일 HTML로 담은 열람 페이지다.

- **열람 링크 (직원 공유용)**: https://cescomktsh-wq.github.io/cesco-templates/
- 이전 배포처였던 Claude 아티팩트(cb7f4d40)는 이 저장소로 이관됐다. 앞으로 링크는 위 GitHub Pages 주소를 쓴다.

## 갱신 방법

`index.html` 하나가 전부다. 수정 → 커밋 → 푸시하면 1분 안에 반영된다.

```powershell
# 수정 후
git add index.html
git commit -m "무엇을 바꿨는지 한 줄"
git push origin main
```

Claude Code에서 갱신을 시킬 때는 이렇게 요청하면 된다:
> `~/cesco-templates/index.html`의 {문서 id}에 {내용}을 반영하고 커밋·푸시해줘.

## 문서 구조 (편집 시 지킬 것)

- 문서 1건 = `<article class="doc" id="dNN" hidden>` 1개. 새 문서는 마지막 article 뒤에 추가하고 id를 이어 쓴다 (현재 마지막: d95).
- 새 문서를 추가하면 4곳을 함께 갱신한다: ① 좌측 내비(`navitem`, `data-goto`/`data-search`) ② d00 마스터 인덱스 표 ③ 하단 스크립트의 `var SECS`(섹션 메뉴) ④ 그룹 헤더의 타입 개수.
- 문서 내 상호 참조는 `<button class="xref" data-goto="dNN">`.
- 상태 뱃지: `s-ok`(정본/실제 확인) · `s-warn`(혼재) · `s-est`(추정).

## 이력

- 2026-08-24: 아티팩트에서 GitHub Pages로 이관. d95 "제품 POP — 제품 부착형 정본 (비주얼 가이드 v.4 전사)" 추가, d45·d77(추정 POP)에 정본 참조 연결. 전사 원문 MD는 cesco-skills 저장소 `cesco-pop/references/`.
