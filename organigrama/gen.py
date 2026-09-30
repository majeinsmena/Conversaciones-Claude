import html
W=2070
COL=[("#fff4e0","#e0a030"),("#e4f3e4","#3c8c3c"),("#e6eefb","#3b6cb7"),("#f1e8fa","#7a4ab0"),("#eaf1dc","#6f8f2a"),("#fde8f1","#c0478a"),("#e3f4f4","#2a8c8c")]
GREEN=("#e4f3e4","#3c8c3c")
def esc(s):return html.escape(s)
class S:
    def __init__(s):s.o=[]
    def box(s,x,y,w,h,title,lines=(),fill="#fff",stroke="#333",dashed=False,pending=False,tsize=17,lsize=13):
        if pending: fill,stroke,dashed="#fff7d6","#d08a00",True
        d=' stroke-dasharray="7 5"' if dashed else ''
        s.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2.2"{d}/>')
        n=1+len(lines);lh=lsize+4;th=tsize+4
        ty=y+(h-(th+len(lines)*lh))/2+tsize
        s.o.append(f'<text x="{x+w/2}" y="{ty}" text-anchor="middle" font-weight="700" font-size="{tsize}" fill="#1b2a41">{esc(title)}</text>')
        for i,l in enumerate(lines):
            c="#b06a00" if "Por designar" in l else "#333"
            wt="700" if "Por designar" in l else "400"
            s.o.append(f'<text x="{x+w/2}" y="{ty+th+i*lh-2}" text-anchor="middle" font-size="{lsize}" fill="{c}" font-weight="{wt}">{esc(l)}</text>')
    def line(s,x1,y1,x2,y2,dashed=False):
        d=' stroke-dasharray="7 5"' if dashed else ''
        s.o.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#555" stroke-width="2" fill="none"{d}/>')
    def text(s,x,y,t,size=14,anchor="middle",weight="400",fill="#333"):
        s.o.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}">{esc(t)}</text>')

def build(func):
    s=S()
    title="ORGANIGRAMA FUNCIONAL PROPUESTO (con nombres y funciones)" if func else "ORGANIGRAMA ESTRUCTURAL PROPUESTO (sin nombres)"
    H=1700 if func else 1300
    s.text(W/2,42,"CODELITESA S.A. – SUPERMERCADOS MI CASERITA",30,weight="700",fill="#1b2a41")
    s.text(W/2,74,title,19,weight="600",fill="#555")
    cx=W/2
    # Junta
    s.box(cx-200,100,400,62 if not func else 76,"JUNTA GENERAL DE ACCIONISTAS",["Familia propietaria – define estrategia y nombra la auditoría"] if func else [],*GREEN[:0],fill="#fde9e9",stroke="#b84a4a")
    jb=100+(76 if func else 62)
    # auditoria
    s.box(cx+380,100,440,76 if func else 62,"AUDITORÍA EXTERNA / CONTROL INTERNO",["Por designar (control interno) – reporta a la Junta","Verifica cajas, inventarios y procedimientos"] if func else ["Reportan a la Junta (independientes)"],fill="#eef",stroke="#555",dashed=True,pending=False,tsize=16)
    s.line(cx+200,100+ (38 if func else 31),cx+380,100+(38 if func else 31),True)
    # Presidencia
    py=jb+36
    s.line(cx,jb,cx,py)
    s.box(cx-200,py,400,80 if func else 56,"PRESIDENCIA",["Martha Hidalgo","Estrategia, supervisión y relación con la Junta"] if func else [],fill="#e4f3e4",stroke="#3c8c3c")
    pb=py+(80 if func else 56)
    gy=pb+36
    s.line(cx,pb,cx,gy)
    s.box(cx-200,gy,400,90 if func else 56,"GERENCIA GENERAL",["Luis Teneda","Dirección de la operación, planificación,","control y representación legal"] if func else [],fill="#e6eefb",stroke="#3b6cb7")
    gb=gy+(90 if func else 56)
    # columns
    w,gap,x0=272,14,40
    hy=gb+52
    hh=120 if func else 70
    bus=gb+26
    s.line(cx,gb,cx,bus)
    cols=[
     ("SUPERMERCADOS MI CASERITA",["Mauro Carvajal","Jefe de Supermercados","13 locales: ventas y servicio"],"13 locales",[
        ("Supervisoras",["Daniela Vidal / Vanessa Yanchapanta","Visitas y control de los locales"],0),
        ("Administradores de local (13)",["Apertura, caja, personal e","inventario de cada local"],0),
        ("Asistentes administrativos (13)",["Uno por local","Apoyo administrativo al administrador"],1),
        ("Percheros, cajeros y bodega",["Atención al cliente, reposición","y manejo de caja"],0)]),
     ("COMERCIAL Y COMPRAS",["Luis David Teneda","Jefe comercial y de compras","Compras, precios y abastecimiento"],"",[
        ("Compras y proveedores",["Mauro Carvajal","Negociación, compras y precios"],0),
        ("Compras y proveedores",["Verónica Teneda","Negociación, compras y precios"],0),
        ("Marketing y publicidad",["Verónica Teneda (supervisa)","Contrata proveedor externo de marketing"],0),
        ("Logística y bodega central",["Jorge Leime","Abastecimiento a los 13 locales"],0)]),
     ("DISTRIBUCIÓN",["Luis David Teneda","Jefe de Agencia Pingüino y","línea Unilever"],"",[
        ("Agencia Pingüino y línea Unilever",["Administrador: Juan Carlos Vallejo","Rutas, cartera y cadena de frío"],0),
        ("Vendedores",["Por designar","Venta en ruta y atención a clientes"],1),
        ("Choferes",["Por designar","Transporte y entrega de pedidos"],1),
        ("Despachadores",["Por designar","Preparación y despacho de pedidos"],1)]),
     ("AGROINDUSTRIA",["Por designar","Distribución de pollo y verduras","a los supermercados"],"",[
        ("Distribución avícola",["Alexis Chiluiza y Javier (*)","Distribución del pollo"],0),
        ("Distribución de verduras",["Rocío Gamboa y Luis Padilla (*)","Abastecimiento de verduras"],0),
        ("Pesados",["Alexis Chiluiza y Javier (*)","Pesado y despacho"],0)]),
     ("PRODUCCIÓN",["Crianza y faenamiento de pollo:","granja, proceso y transporte"],"",[
        ("Jefe de granja",["Oliver Tipán","Coordinación de la granja,","bioseguridad y personal"],0),
        ("Galponero y asistente de granja",["Por designar","Cuidado de aves,","alimentación y registros"],1),
        ("Faenadores y preparados",["Por designar","Faenado, proceso y","empaque del pollo"],1),
        ("Choferes de producción",["Por designar","Traslado, refrigerado","y entrega del pollo"],1)]),
     ("TALENTO HUMANO",["Fernanda Teneda","Jefa de Talento Humano","Personal de todas las unidades"],"",[
        ("Selección y contratación",["Fernanda Teneda","Reclutamiento e ingreso de personal"],0),
        ("Nómina y beneficios",["Fernanda Teneda","Pago de personal y beneficios"],0),
        ("Capacitación y desarrollo",["Fernanda Teneda","Formación y clima laboral"],0),
        ("Asistente del departamento",["Por designar","Apoyo administrativo a Talento Humano"],1)]),
     ("ADMINISTRACIÓN Y FINANZAS",["Martha Hidalgo","Jefa financiera","Servicios administrativos y de apoyo"],"",[
        ("Contabilidad",["2 jefaturas (contable e inventarios)","y 7 puestos de equipo"],0,[
            ("Jefatura contable",["Martha Ramírez"],0,1),
            ("Contadora general",["Verónica Teneda"],0,2),
            ("Técnico contable",["Cuadre de caja","Por designar"],1,2),
            ("Técnico contable",["Comprobantes","Por designar"],1,2),
            ("Técnico contable",["Efectivizaciones","Por designar"],1,2),
            ("Jefatura de inventarios",["Paulina Gamboa"],0,1),
            ("Asistente contable",["Ingreso de compras","Por designar"],1,2),
            ("Asistente contable",["Manejo de matriz","Por designar"],1,2),
            ("Asistente contable",["Bodegas y negociación","Por designar"],1,2)]),
        ("Tesorería",["Por designar","Cobros, pagos y bancos"],1),
        ("Sistemas",["Ing. Jaime Pinela","Soporte tecnológico y redes"],0),
        ("Mant., seguridad y limpieza",["Mantenimiento, seguridad","y limpieza de instalaciones"],0)])]
    for i,(t,ls,_,ch) in enumerate(cols):
        ch=[c if len(c)==4 else c+(None,) for c in ch]
        x=x0+i*(w+gap);mx=x+w/2
        s.line(mx,bus,mx,hy) ; 
        fill,stroke=COL[i]
        pend=("Por designar" in ls[0]) if func else False
        s.box(x,hy,w,hh,t,ls if func else [],fill=fill,stroke=stroke,pending=pend,tsize=16)
        y=hy+hh
        chh=84 if func else 46
        cg=20
        for (ct,cl,cp,subs) in ch:
            s.line(mx,y,mx,y+cg)
            y+=cg
            s.box(x+10,y,w-20,chh,ct,cl if func else [],fill=fill,stroke=stroke,pending=bool(cp) and func,tsize=14.5,lsize=12)
            y+=chh
            if subs:
                sg=8; pos=[]
                y+=10
                for (st,sl,sp,lv) in subs:
                    sh=(40 if func else 34) if lv==1 else (52 if func else 44)
                    ind=34 if lv==1 else 52
                    pend="Por designar" in sl[-1]
                    if func: s.box(x+ind,y,w-ind-14,sh,st,sl,fill="#fff",stroke=stroke,pending=pend,tsize=12.5,lsize=11)
                    else: s.box(x+ind,y,w-ind-14,sh,st,sl[:1] if (lv==2 and len(sl)>1 and "Por designar" in sl[-1]) else [],fill="#fff",stroke=stroke,tsize=12.5,lsize=11)
                    pos.append((y,sh,lv)); y+=sh+sg
                l1=[p for p in pos if p[2]==1]
                s.line(x+22,pos[0][0]-10,x+22,l1[-1][0]+l1[-1][1]/2)
                for (py_,ph,lv) in l1: s.line(x+22,py_+ph/2,x+34,py_+ph/2)
                for k,(py_,ph,lv) in enumerate(pos):
                    if lv==1:
                        kids=[]
                        for q in pos[k+1:]:
                            if q[2]==1: break
                            kids.append(q)
                        if kids:
                            s.line(x+46,py_+ph,x+46,kids[-1][0]+kids[-1][1]/2)
                            for q in kids: s.line(x+46,q[0]+q[1]/2,x+52,q[0]+q[1]/2)
                y+=2
    xs=[x0+i*(w+gap)+w/2 for i in range(7)]
    s.line(xs[0],bus,xs[-1],bus)
    # legend
    ly=H-96
    s.box(40,ly,760,70,"",[],fill="#fafafa",stroke="#999",tsize=14);s.text(420,ly+20,"SIMBOLOGÍA",14,weight="700")
    s.line(60,ly+46,110,ly+46);s.text(118,ly+51,"Línea de autoridad",13,"start")
    s.line(270,ly+46,320,ly+46,True);s.text(328,ly+51,"Asesoría / control independiente",13,"start")
    s.o.append(f'<rect x="590" y="{ly+36}" width="34" height="20" rx="4" fill="#fff7d6" stroke="#d08a00" stroke-width="2" stroke-dasharray="5 3"/>')
    s.text(632,ly+51,"Por designar",13,"start");s.text(40,ly-10,"(*) Apellido por confirmar",12,"start")
    if func: s.box(840,ly,920,70,"PROPÓSITO",["Brindar a nuestros clientes productos de calidad, con excelente servicio y los mejores precios."],fill="#eef4fb",stroke="#3b6cb7",tsize=14)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif"><rect width="100%" height="100%" fill="#fff"/>'+"".join(s.o)+'</svg>'
open("organigrama_estructural_propuesto.svg","w").write(build(False))
open("organigrama_funcional_propuesto.svg","w").write(build(True))
