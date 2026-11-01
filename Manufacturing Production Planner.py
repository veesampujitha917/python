
def planner():
    p={"Chair":{"demand":100,"stock":30,"m":2,"planned":80,"def":4},"Table":{"demand":50,"stock":10,"m":5,"planned":45,"def":6},"Shelf":{"demand":70,"stock":20,"m":3,"planned":60,"def":2}}
    total=0
    for n,d in p.items():
        m=d["planned"]*d["m"]; total+=m
        g=d["planned"]-d["def"]; a=d["stock"]+g; s=max(0,d["demand"]-a); r=(d["def"]/d["planned"])*100
        print(f"\nProduct: {n}\nMaterial required: {m}\nGood units produced: {g}\nTotal available: {a}\nDemand shortage: {s}\nDefect rate: {r:.2f}%\nQuality: {'VIOLATION' if r>5 else 'OK'}")
    print(f"\nTotal material required: {total}\nMaterial feasibility: {'FEASIBLE' if total<=600 else 'SHORTAGE'}")

planner()
