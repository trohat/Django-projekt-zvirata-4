"""
CRUD

#CREATE:
opice = Zvire(jmeno="Jitka", druh="gorila", vek=13, popis="Má ráda banány")
opice.save()

nebo zkratka:
Zvire.objects.create(druh="Člověk", jmeno="Adam", popis="Je to alfasamec.", vek=30)

#READ:
Zvire.objects.all()
Zvire.objects.get(jmeno="Alík") 
Zvire.objects.get(id=3) 
Zvire.objects.get(pk=4) 
Zvire.objects.filter(jmeno="Alík").filter(vek__gte=10).filter(popis__contains="hlídá")


#UPDATE:
opice.jmeno = "Táňa"
opice.save()

#DELETE:
opice.delete()


"""