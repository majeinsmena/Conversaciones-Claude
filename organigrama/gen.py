import html
W=1800
COL=[("#fff4e0","#e0a030"),("#e4f3e4","#3c8c3c"),("#e6eefb","#3b6cb7"),("#f1e8fa","#7a4ab0"),("#e3f4f4","#2a8c8c")]
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
    H=1330 if func else 960
    s.text(W/2,42,"CODELITESA S.A. – SUPERMERCADOS MI CASERITA",30,weight="700",fill="#1b2a41")
    s.text(W/2,74,title,19,weight="600",fill="#555")
    cx=W/2
    # Junta
    s.box(cx-200,100,400,62 if not func else 76,"JUNTA GENERAL DE ACCIONISTAS",["Familia propietaria – define estrategia y nombra la auditoría"] if func else [],*GREEN[:0],fill="#fde9e9",stroke="#b84a4a")
    jb=100+(76 if func else 62)
    # auditoria
    s.box(1280,100,440,76 if func else 62,"AUDITORÍA EXTERNA / CONTROL INTERNO",["Por designar (control interno) – reporta a la Junta","Verifica cajas, inventarios y procedimientos"] if func else ["Reportan a la Junta (independientes)"],fill="#eef",stroke="#555",dashed=True,pending=False,tsize=16)
    s.line(cx+200,100+ (38 if func else 31),1280,100+(38 if func else 31),True)
    # Presidencia
    py=jb+36
    s.line(cx,jb,cx,py)
    s.box(cx-200,py,400,80 if func else 56,"PRESIDENCIA",["Marta Hidalgo","Estrategia, supervisión y relación con la Junta"] if func else [],fill="#e4f3e4",stroke="#3c8c3c")
    pb=py+(80 if func else 56)
    gy=pb+36
    s.line(cx,pb,cx,gy)
    s.box(cx-200,gy,400,90 if func else 56,"GERENCIA GENERAL",["Luis Teneda","Dirección de la operación, planificación,","control y representación legal"] if func else [],fill="#e6eefb",stroke="#3b6cb7")
    gb=gy+(90 if func else 56)
    # columns
    w,gap,x0=320,30,40
    hy=gb+52
    hh=120 if func else 70
    bus=gb+26
    s.line(cx,gb,cx,bus)
    cols=[
     ("SUPERMERCADOS MI CASERITA",["Mauro Carvajal","13 locales: ventas, servicio y","cumplimiento de políticas"],"13 locales",[
        ("Supervisoras",["Daniela Vidal / Vanessa (apellido por confirmar)","Visitas y control de los locales"],0),
        ("Administradores de local (13)",["Apertura, caja, personal e","inventario de cada local"],0),
        ("Percheros, cajeros y bodega",["Atención al cliente, reposición","y manejo de caja"],0),
        ("Control de inventarios y mermas",["Por designar","Conteos, vencimientos y pérdidas"],1)]),
     ("COMERCIAL Y COMPRAS",["Por designar","Margen: negociación con proveedores,","precios y abastecimiento"],"",[
        ("Compras y proveedores",["Por designar","Negociación y compras por volumen"],1),
        ("Precios y ofertas",["Por designar","Lista de precios y promociones"],1),
        ("Marketing y publicidad",["Por designar","Ofertas semanales, volantes, fidelización"],1),
        ("Logística y bodega central",["Por designar","Abastecimiento a los 13 locales"],1)]),
     ("DISTRIBUCIÓN",["Luis David Teneda","Distribución, cartera y rutas"],"",[
        ("Agencia Pingüino",["Luis David Teneda","Distribución, rutas y cadena de frío"],0),
        ("Línea Unilever",["Luis David Teneda","Desarrollo de la línea de distribución"],0)]),
     ("AGROINDUSTRIA",["Por designar","Abastece a los supermercados","con producto propio"],"",[
        ("Producción avícola",["Engorde y planta de proceso","Responsable por designar"],1),
        ("Línea de verduras",["Cultivo y abastecimiento","Responsable por designar"],1),
        ("Piscicultura",["Producción y manejo de truchas","Responsable por designar"],1)]),
     ("ADMINISTRACIÓN Y FINANZAS",["Verónica Teneda","Contabilidad, tesorería y","servicios compartidos"],"",[
        ("Contabilidad y tributaria",["Asistentes contables (6)","Registro, conciliaciones, reportes"],0),
        ("Tesorería",["Por designar","Cobros, pagos y bancos"],1),
        ("Talento Humano",["Fernanda Teneda","Selección, nómina, capacitación"],0),
        ("Sistemas",["Ing. Jaime Pinela","Soporte tecnológico y redes"],0),
        ("Mantenimiento, seguridad y limpieza",["Preventivo/correctivo, control","de instalaciones y sanidad"],0)])]
    for i,(t,ls,_,ch) in enumerate(cols):
        x=x0+i*(w+gap);mx=x+w/2
        s.line(mx,bus,mx,hy) ; 
        fill,stroke=COL[i]
        pend=("Por designar" in ls[0]) if func else False
        s.box(x,hy,w,hh,t,ls if func else [],fill=fill,stroke=stroke,pending=pend,tsize=16)
        y=hy+hh
        chh=84 if func else 46
        cg=20
        for (ct,cl,cp) in ch:
            s.line(mx,y,mx,y+cg)
            y+=cg
            s.box(x+10,y,w-20,chh,ct,cl if func else [],fill=fill,stroke=stroke,pending=bool(cp) and func,tsize=14.5,lsize=12)
            y+=chh
    xs=[x0+i*(w+gap)+w/2 for i in range(5)]
    s.line(xs[0],bus,xs[-1],bus)
    # legend
    ly=H-96
    s.box(40,ly,760,70,"",[],fill="#fafafa",stroke="#999",tsize=14);s.text(420,ly+20,"SIMBOLOGÍA",14,weight="700")
    s.line(60,ly+46,110,ly+46);s.text(118,ly+51,"Línea de autoridad",13,"start")
    s.line(270,ly+46,320,ly+46,True);s.text(328,ly+51,"Asesoría / control independiente",13,"start")
    s.o.append(f'<rect x="590" y="{ly+36}" width="34" height="20" rx="4" fill="#fff7d6" stroke="#d08a00" stroke-width="2" stroke-dasharray="5 3"/>')
    s.text(632,ly+51,"Por designar",13,"start")
    if func: s.box(840,ly,920,70,"PROPÓSITO",["Brindar a nuestros clientes productos de calidad, con excelente servicio y los mejores precios."],fill="#eef4fb",stroke="#3b6cb7",tsize=14)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif"><rect width="100%" height="100%" fill="#fff"/>'+"".join(s.o)+'</svg>'
open("organigrama_estructural_propuesto.svg","w").write(build(False))
open("organigrama_funcional_propuesto.svg","w").write(build(True))
