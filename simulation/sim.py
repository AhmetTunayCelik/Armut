# Monte Carlo of incremental event requests per year for each solution.
# Volumes = Armut pro-page "Yılda N ... müşterisi" (Fact, Türkiye, checked 2026-11-07).
# Every rate is an ASSUMPTION given as a triangular range (low, mode, high). Not a forecast.
import numpy as np, json
rng=np.random.default_rng(42); N=100_000
V=dict(pasta=18184,nisan_org=12918,dg_pasta=8963,catering=8032,palyaco=7633,dg_org=7076,masa_sandalye=5379,
       butik_pasta=5292,gelin_arabasi=3446,dugun_foto=2947,kina_org=2897,nisan_foto=2557,sandalye=2094,dugun_org=2026,
       animator=1540,ses_sistemi=1541,ceyiz=1522,sunnet_org=1419,balon=1382,cleaning=84391,moving=186667,mobilya=8376,yat=8792,tekne=7737,dugun_salonu=4114)
birthday=V['pasta']+V['dg_pasta']+V['dg_org']+V['palyaco']+V['butik_pasta']+V['animator']+V['balon']
wedding=V['dugun_salonu']+V['nisan_org']+V['kina_org']+V['dugun_org']+V['dugun_foto']+V['nisan_foto']+V['gelin_arabasi']+V['ceyiz']
hosting=V['masa_sandalye']+V['sandalye']+V['catering']+V['ses_sistemi']
boats=V['yat']*0.52+V['tekne']*0.33  # measured event share in Istanbul samples (11/21, 7/21)
event_total=birthday+wedding+V['sunnet_org']+V['masa_sandalye']+V['sandalye']+V['catering']+V['ses_sistemi']+boats
T=lambda a,m,b: rng.triangular(a,m,b,N)
S={}
# 1 Next-for-your-party card (birthday cluster)
cake=V['pasta']+V['dg_pasta']+V['butik_pasta']; party=V['dg_org']+V['palyaco']+V['animator']+V['balon']
# CTR priors anchored on measured second-need mentions in free text (handoff 19): cake 6-8%, birthday org 17-21%, nisan org 12-44%
S['A1 Party card after birthday-type requests']=dict(
 v=(cake*T(.005,.02,.04)+party*T(.02,.05,.09))*T(.7,.85,.95)*T(.40,.52,.62)*T(.5,.7,.9), reach=birthday, effort=2, risk=2, conf=3,
 p=0.03, d=0.02, note='CTR split: cake (focused buyers) vs organization/palyaco (mention 2nd needs 17-21%)')
# 2 Next-for-your-wedding card (nisan/kina/dugun cluster incl. ceyiz)
S['A2 Wedding card after nisan/kina/wedding/ceyiz requests']=dict(
 v=(V['nisan_org']*T(.02,.05,.09)+(wedding-V['nisan_org'])*T(.01,.025,.05))*T(.7,.85,.95)*T(.40,.50,.62)*T(.5,.7,.9), reach=wedding, effort=1, risk=2, conf=3,
 p=0.03,d=0.02, note='same card component, second entry point')
# 3 Hosting bridge (masa sandalye etc.) measured event share 37% for masa sandalye
S['A3 Hosting bridge from masa-sandalye/catering/ses sistemi/yat/tekne']=dict(
 v=(hosting*T(.30,.40,.55)+boats)*T(.03,.07,.12)*T(.40,.52,.62)*T(.6,.8,.95), reach=hosting+boats, effort=1, risk=2, conf=4,
 p=0.03,d=0.02, note='event-intent share measured 37% (27/73) on masa sandalye; others assumed lower')
# 4 Keyword trigger from cleaning/moving (measured 0/315) - kept to show why it ranks low
S['X1 Keyword trigger from cleaning/moving free text']=dict(
 v=(V['cleaning']+V['moving']+V['mobilya'])*T(0,.002,.01)*T(.05,.10,.15)*T(.3,.42,.55)*T(.6,.8,.95),
 reach=V['cleaning']+V['moving']+V['mobilya'], effort=2, risk=3, conf=4, p=0.001,d=0.001, note='0 of 315 sample texts mention an event')
# 5 Price/local page upgrade: share of event requests that start on SEO pages x relative lift
S['B1 Event price/local page upgrade (occasion links, proof, sticky CTA)']=dict(
 v=event_total*T(.15,.30,.50)*T(.02,.06,.15)*T(.4,.6,.8)*T(.7,.85,1.0), reach=event_total, effort=2, risk=1, conf=2,
 p=0.05,d=0.005, note='SEO-origin share and lift both assumed')
# 6 Abandoned event start recovery
c=T(.40,.55,.70)
S['B2 Recover abandoned event request starts']=dict(
 v=event_total*(1/c-1)*T(.05,.12,.25)*T(.04,.08,.15)*T(.6,.8,.95), reach=event_total, effort=1.5, risk=1, conf=2,
 p=0.05,d=0.03, note='sign-up is the LAST step (audit), so only logged-in/app abandoners are reachable; completion, reach, return assumed')
# 7 Birthday comeback reminder
S['C1 Birthday comeback reminder (11 months later)']=dict(
 v=birthday*T(.30,.45,.60)*T(.15,.25,.40)*T(.03,.06,.10)*T(.4,.6,.8), reach=birthday*0.45*0.25, effort=1, risk=1, conf=2,
 p=0.06,d=0.03, note='repeat-occasion share, reachable, conversion, incrementality assumed')
# 8 Seasonal homepage/app slot (net of cannibalization)
S['C2 Seasonal event slot on homepage/app']=dict(
 v=event_total*T(.005,.02,.05)*T(.3,.6,.9)*T(.25,.33,.5), reach=event_total, effort=1, risk=2, conf=1,
 p=0.05,d=0.003, note='relative lift on event base, net of cannibalization; homepage traffic unknown')
# 9 Cost report for press (earned PR)
S['C3 "2026 nisan/kina/dugun maliyeti" press report']=dict(
 v=T(50,300,1500), reach=None, effort=0.5, risk=1, conf=1, p=None,d=None, note='pickups x visits x conversion; no data')
# 10 Office year-end pack to business customers
S['C4 Office year-end event pack (B2B CRM)']=dict(
 v=(V['cleaning']+V['moving'])*T(.01,.03,.06)*T(.4,.6,.8)*T(.01,.03,.06), reach=(V['cleaning']+V['moving']), effort=0.5, risk=1, conf=1,
 p=0.01,d=0.01, note='business share, reachable, conversion assumed')
# 11 Kres-friendly birthday cake variant
S['C5 Kres/school birthday cake variant']=dict(
 v=(V['dg_pasta']+V['pasta']*0.5+V['butik_pasta']*0.5)*T(.2,.35,.5)*T(.02,.05,.10), reach=V['dg_pasta'], effort=1, risk=1, conf=1,
 p=0.05,d=0.005, note='child share and uplift assumed')
# 12 WhatsApp concierge (capped by ops)
S['C6 WhatsApp concierge on event pages (ops-capped)']=dict(
 v=np.minimum(T(600,1800,4800), (event_total/T(.05,.10,.15))*T(.01,.02,.03)*T(.3,.45,.6)*T(.3,.45,.6)), reach=None, effort=1.5, risk=2, conf=1, p=None,d=None,
 note='effort includes ops hours (~0.5 FTE); capped at 50-400 requests/month ops capacity')
# 14 Discovery entry for NEW users: 1-2 event services in homepage trending/popular lists and the search empty state ("Önerilen hizmetler"), seasonal rotation; plus search synonym fixes (e.g. takı töreni -> photographer)
S['D1 Event entry in homepage lists + search empty state (new users)']=dict(
 v=event_total*T(.005,.02,.05)*T(.3,.6,.9), reach=event_total*10, effort=1, risk=2, conf=2,
 p=0.05,d=0.005, note='always-on merchandising; relative lift on event base net of clicks taken from core; homepage traffic unknown (reach assumed 10x event base)')
# 13 Copy angle test - learning value, small direct volume
S['B3 Copy angle test (awareness vs trust vs speed)']=dict(
 v=T(0,150,800), reach=None, effort=0.5, risk=1, conf=2, p=None,d=None, note='direct volume small; value is choosing the message for B1/C1/C2')
rows=[]
for k,s in S.items():
  v=s['v']; p10,p50,p90=np.percentile(v,[10,50,90])
  # test duration: n per arm = 16 p(1-p)/d^2 ; weekly exposed = reach/52 ; 50/50 split
  wk=None
  if s.get('p') and s.get('reach'):
    n=16*s['p']*(1-s['p'])/s['d']**2; wk=round(2*n/(s['reach']/52),1)
  score=p50*s['conf']/(s['effort']*s['risk'])
  rows.append(dict(name=k,p10=int(p10),p50=int(p50),p90=int(p90),share_of_event_base=round(100*p50/event_total,2),
    effort=s['effort'],risk=s['risk'],conf=s['conf'],weeks_to_detect=wk,score=round(score),note=s['note']))
rows.sort(key=lambda r:-r['score'])
print('boats',boats,'birthday cluster',birthday,'wedding cluster',wedding,'hosting',hosting,'event total',event_total)
for r in rows: print(r)
json.dump(dict(birthday=birthday,wedding=wedding,hosting=hosting,event_total=event_total,rows=rows),open('/mnt/user-data/outputs/sim/results.json','w'),indent=1)

# ---------- Part 2: testability-adjusted ranking, programs, sensitivity, pro-cost guardrail ----------
def testf(w):
  if w is None: return 0.5
  return 1.0 if w<=4 else (0.7 if w<=12 else 0.35)
for r in rows: r['testability']=testf(r['weeks_to_detect']); r['rank_score']=round(r['p50']*r['conf']*r['testability']/(r['effort']*r['risk']))
# programs (shared component -> shared effort)
card=S['A1 Party card after birthday-type requests']['v']+S['A2 Wedding card after nisan/kina/wedding/ceyiz requests']['v']+S['A3 Hosting bridge from masa-sandalye/catering/ses sistemi/yat/tekne']['v']
crm=S['C1 Birthday comeback reminder (11 months later)']['v']+S['B2 Recover abandoned event request starts']['v']
prog={'P1 Card program (A1+A2+A3, one component, 3 entry points)':card,'P2 Lifecycle CRM (B2+C1)':crm}
progrows=[]
for k,v in prog.items():
  p10,p50,p90=np.percentile(v,[10,50,90]); progrows.append(dict(name=k,p10=int(p10),p50=int(p50),p90=int(p90),share=round(100*p50/event_total,2)))
top5=card+crm+S['B1 Event price/local page upgrade (occasion links, proof, sticky CTA)']['v']
top5o=top5*T(.75,.85,.95) # overlap discount
progrows.append(dict(name='All of P1+P2+B1 with 5-25% overlap discount',p10=int(np.percentile(top5o,10)),p50=int(np.percentile(top5o,50)),p90=int(np.percentile(top5o,90)),share=round(100*np.percentile(top5o,50)/event_total,2)))
# sensitivity for A1: one-at-a-time low/high around modes
def a1(seen=.85,ctr=.04,sub=.52,inc=.7): return birthday*seen*ctr*sub*inc
base=a1(); sens={'card seen (.7-.95)':(a1(seen=.7),a1(seen=.95)),'CTR (1%-8%)':(a1(ctr=.01),a1(ctr=.08)),'submit after click (40-62%)':(a1(sub=.40),a1(sub=.62)),'incrementality (50-90%)':(a1(inc=.5),a1(inc=.9))}
# pro cost guardrail for card program: extra requests x quotes x fee x (1-hire)
q=T(2,3.5,5); fee=T(150,400,800); hire=T(.15,.25,.40)
waste=card*q*fee*(1-hire)
pro_cost=dict(p10=int(np.percentile(waste,10)),p50=int(np.percentile(waste,50)),p90=int(np.percentile(waste,90)))
json.dump(dict(birthday=birthday,wedding=wedding,hosting=hosting,event_total=event_total,rows=sorted(rows,key=lambda r:-r['rank_score']),programs=progrows,
  a1_base=round(base),a1_sensitivity={k:[round(a),round(b)] for k,(a,b) in sens.items()},pro_cost_TL=pro_cost),open('results.json','w'),indent=1,default=float)
for r in sorted(rows,key=lambda r:-r['rank_score']): print(r['rank_score'],r['name'],r['p50'],r['weeks_to_detect'])
print(progrows); print('A1 base',round(base),sens); print('pro cost TL/yr on card leads',pro_cost)
