#!/usr/bin/python3

#   Este programa genera archivos CSV de 4 valores por registro para fusiones en corel
#   Copyright (C) 2024 Cristian Tocci

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

#   Contacto : toccicristian@hotmail.com / toccicristian@protonmail.ch


licencias=dict()
licencias['gplv3']="""
    csv_dosposes.py  Copyright (C) 2024  Cristian Tocci
    This program comes with ABSOLUTELY NO WARRANTY; for details
    press `Ctrl + w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; See COPYING.odt file for further details.
    """
licencias['gplv3logo']="""
+----------------------------------------------------------------------------------------------------+
|oooooooo+~~~+~~~~~~+~~~~~+~~~~+~~~~~~+~~~~+~~~~~~+~~+~~~~+~~~~~+~~~~+~~~~~~++~~+~~+~~~~~~:  ::::::~+|
|oooooooo :::::::::::::::::::::::::::::::::::::::::::~::::::::::::::::::::::::::::::::. ~~~++ooooo+:.|
|ooooooo~::::::~:::::::::::::::::::::::::::::::::::::+::::::::::::::::::::::::~~.~:~:~+oooooooooooo:.|
|ooooooo :~:~~~~~~~~~~+~::: +~~~~~~~~~~~~~::++ :::::~+~:::::::::::::::::::~...~:::~ooooooooooooooo~.+|
|oooooo~~:~oo~~~~~~~~~oo~:~+oo ~~~~~~.ooo.~oo+~::::.+o ::::::::::::::::~  .~::::+oo+~:   +ooooooo::+o|
|oooooo::.+o+~::::::~+oo : oo~::::::::oo~:~oo~::::: oo~:::::::::::::: ~ ~::::.++~ ~:::::.+oooo+~ ~ooo|
|ooooo+~:~oo~:::::::::::::~oo::::::::+oo :+oo~:::::~oo+.::::::::::.:~ ~:::::: .:::::::~~oooo+:~ +oooo|
|ooooo::~+o+.:::::::::::: oo+~:::::: oo~~:oo~::::::~ooo~::::::::.~~.::::::::::::::::~~+oooooo+~::oooo|
|oooo+~::oo~:::~:~:~~::::~oo~       ~oo::+oo.::::::~ooo+~::::: ~~.:::::::::::::::: ~+oooooooooo~~oooo|
|oooo~::+oo :::~   +oo::.ooo~~~~~~~~~:.: oo+:::::::~oooo~:::~~+:::::::::::::::: ~+++~~~~oooooo+.~oooo|
|ooo+.: oo~:::::::.oo+.:~oo~::::::::::::~oo:::::::::oooo+~::++~::::::::::::::~   .::::::ooooo~.~ooooo|
|ooo~::~oo::::::::~oo~:~+o+~::::::::::: oo+~:::::::.+ooo~.~o+:::::::::::::::::::::::: +oooo+: +oooooo|
|ooo.: oo+.~~~~~~ +oo.::oo~::::::::::::~oo~~~~~~~:::+oo~ +oo ::::::::::::::::::::.:~ooooo+: ~oooooooo|
|oo~::.~~~~~~~~~~~~~ ::~+~.::::::::::::~+~~~~~~~~~:::o~ +ooo:::::::::::::::::: ~+oooooo~::~oooooooooo|
|o+ :~   ~::::::::::::.  ~::::: ..:::::::::::::::::::~ ~oooo~~::::::::::~. ~~+oooooo+~::+oooooooooooo|
|o~~:~~: ~ :~~. ~~.::~~~~. ::.~~~~::~:: :~~.~::~~ ::::.oooooo+~~::::~~~~ooooooooo+~::~+oooooooooooooo|
|o::~~~~:::~~~ ~~~.:: ::~.~:~.~~~: ~~~ :~~~: ~~~~~:::: oooooooooooooooooooooo++~::~+ooooooooooooooooo|
|+:::~::::::~~::::::::~~:::~::~:::::::::::~::::~:::::::~ooooooooooooooooo++~::~~+oooooooooooooooooooo|
|::::::::::::::::::::::::::::::::::::::::::::::::::::::: ~oooooooooo+~~~::~~+oooooooooooooooooooooooo|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:~~~~~:    ::::::::~~~ooooooooooooooooooooooooooooo|
+----------------------------------------------------------------------------------------------------+
"""
licencias['textow']="""
    15. Disclaimer of Warranty.
    THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
    APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
    HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT
    WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
    PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE
    OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU
    ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

    16. Limitation of Liability.
    IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
    WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR
    CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR
    DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL
    DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM
    (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED
    INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF
    THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER
    OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

    17. Interpretation of Sections 15 and 16.
    If the disclaimer of warranty and limitation of liability provided above
    cannot be given local legal effect according to their terms,
    reviewing courts shall apply local law that most closely approximates
    an absolute waiver of all civil liability in connection with the Program,
    unless a warranty or assumption of liability accompanies a copy of
    the Program in return for a fee.
    """

import sys
import os
import tkinter.filedialog
import tkinter as tk

default_file=os.path.expanduser(os.path.normpath('~/dosposes-salida.csv'))


def show_w(ventana_principal,textow):
        ventana_w = tkinter.Toplevel(ventana_principal)
        ventana_w.title('This program comes with ABSOLUTELY NO WARRANTY')
        ventana_w.geometry('800x600')
        tkinter.Label(ventana_w,text=textow).pack()
        ventana_w.focus_set()
        ventana_w.bind('<Escape>', lambda event : ventana_w.destroy())


def dialogo_sobreescribir_si_callback (ventana_sobreescribir,logbox,datos=dict()):
    genera_archivo(logbox,datos)
    ventana_sobreescribir.destroy()


def muestra_dialogo_sobreescribir(ventana_principal,logbox,datos=dict()):
    ventana_s = tkinter.Toplevel(ventana_principal)
    ventana_s.title('ATENCION! SOBREESCRIBIR?')
    ventana_s.geometry('300x100')
    ventana_s.resizable(width = False, height = False)
    ventana_s.transient(ventana_principal)
    ventana_s.grab_set()
    ventana_s.bind(
        '<Escape>', lambda event : ventana_s.destroy())
    frame_output = tkinter.Frame(ventana_s)
    frame_input = tkinter.Frame(ventana_s)
    label_pregunta = tkinter.Label(frame_output,
                  text = 'El archivo ya existe. Sobreescribir?')
    button_si = tkinter.Button(frame_input,text = 'SI!  ')
    button_no = tkinter.Button(frame_input,text = 'NO...')
    frame_output.pack(side=tkinter.TOP,pady=(10,5))
    label_pregunta.pack(side=tkinter.LEFT)
    frame_input.pack(side=tkinter.TOP,pady=(5,10))
    button_si.pack(side = tkinter.RIGHT,padx=(5,0))
    button_no.pack(side = tkinter.RIGHT,padx=(0,5))
    button_si.config(command = lambda : dialogo_sobreescribir_si_callback(
        ventana_s, logbox, datos))
    button_no.config(command = lambda : ventana_s.destroy())
    button_si.focus()


def loguea(logbox,linea):
    logbox.configure(state='normal')
    logbox.insert(tk.END,linea)
    logbox.see(tk.END)
    logbox.configure(state='disabled')


def genera_archivo(logbox,datos=dict()):
    with open(str(datos['nombre_archivo']),'w') as ar:
        ciclo=int(0)
        while ciclo < int(datos['ciclos']):
            x = int(datos['desde'])+ciclo
            ar.write(str(x).zfill(int(datos['cantidad_digitos']))+',')
            ar.write(str(int(datos['ciclos']) + x).zfill(int(datos['cantidad_digitos']))+'\n')
            ciclo = ciclo + 1
    loguea(logbox,'Archivo \''+os.path.split(str(datos['nombre_archivo']))[1]+'\' generado.\n')


def convierte_a_dict (entry_desde,entry_intervalo,entry_cantdig,
             entry_ciclos,entry_url,logbox):
    datos=dict()
    datos['desde'] = entry_desde.get()
    datos['intervalo'] = entry_intervalo.get()
    datos['cantidad_digitos'] = entry_cantdig.get()
    datos['ciclos'] = entry_ciclos.get()
    datos['nombre_archivo'] = entry_url.get()
    if not str(datos['nombre_archivo']).endswith('.csv'):
        datos['nombre_archivo']=str(datos['nombre_archivo'])+'.csv'

    campos_int=['desde','intervalo','cantidad_digitos','ciclos']
    for campo_int in campos_int:
        if not str(datos[campo_int]).isdigit():
            loguea(logbox,'Error en '+str(campo_int)+':No es num. entero.\n')
            return False

    if not os.path.isdir(os.path.split(datos['nombre_archivo'])[0]):
            loguea(logbox,'Error : Directorio no existe\n')
            return False

    return datos


def generar (ventana_principal,entry_desde,entry_intervalo,entry_cantdig,
             entry_ciclos,entry_url,logbox):
    d=convierte_a_dict(entry_desde, entry_intervalo, entry_cantdig,
                     entry_ciclos, entry_url, logbox)
    if not d:
        return False
    if os.path.isfile(d['nombre_archivo']):
        muestra_dialogo_sobreescribir(ventana_principal,logbox,d)
        return True
    genera_archivo(logbox,d)
    return True


def directory_browser(titulo=str(),defaultdir=str()):
        if not titulo:
                titulo='Seleccione directorio destino...'
        directorio=tk.filedialog.askdirectory(title=titulo)
        if not directorio:
               directorio=defaultdir
        return os.path.expanduser(os.path.normpath(directorio))


def examinar(entry_url):
    global default_file
    head_url,tail_url=os.path.split(default_file)
    if len(entry_url.get()) != 0:
        if os.path.isdir(os.path.split(os.path.expanduser(os.path.normpath(entry_url.get())))[0]):
            head_url=os.path.split(os.path.expanduser(os.path.normpath(entry_url.get())))[0]
        tail_url=os.path.split(os.path.expanduser(os.path.normpath(entry_url.get())))[1]
    directorio_seleccionado=directory_browser('Seleccione directorio para '+tail_url,head_url)
    entry_url.delete(0,tkinter.END)
    if not directorio_seleccionado:
        directorio_seleccionado = head_url
    entry_url.insert(tkinter.END, os.path.join(directorio_seleccionado,tail_url))
    return


def muestra_ventana():
    global default_file
    v=tk.Tk()
    v.geometry('590x360')
    v.resizable(width=False,height=False)
    v.title('dosposes')

    marco_url=tk.Frame(v)
    marco_url_entry=tk.Frame(marco_url)
    label_url=tk.Label(marco_url_entry,text='Archivo salida:')
    entry_url=tk.Entry(marco_url_entry,width=50)
    entry_url.insert(tk.END,default_file)
    marco_url_boton=tk.Frame(marco_url)
    boton_url=tk.Button(marco_url_boton,text='Examinar...',width=12)

    marco_datos=tk.Frame(v)
    marco_d_labels=tk.Frame(marco_datos)
    marco_d_ingreso=tk.Frame(marco_datos)
    label_desde=tk.Label(marco_d_labels,text='Desde (termina con 1):')
    entry_desde=tk.Entry(marco_d_ingreso)
    label_intervalo=tk.Label(marco_d_labels,text='Intervalo (suele ser 1) :')
    entry_intervalo=tk.Entry(marco_d_ingreso)
    entry_intervalo.insert(tk.END,1)
    label_cantdig=tk.Label(marco_d_labels,text='Cant.Dig.:')
    entry_cantdig=tk.Entry(marco_d_ingreso)
    label_ciclos=tk.Label(marco_d_labels,text='Cant. de registros:')
    entry_ciclos=tk.Entry(marco_d_ingreso)

    marco_botones=tk.Frame(v)
    boton_generar=tk.Button(marco_botones,text='Generar',width=12)
    marco_log=tk.Frame(v)
    logbox=tk.Text(marco_log,height=8,width=65,state='disabled',font=('Helvetica',10))
    logbox_scrollbar=tk.Scrollbar(marco_log)

    v.bind('<Escape>', lambda event :v.destroy())
    v.bind_all('<Control-Key-w>', lambda event :show_w(v, licencias['textow']))
    v.bind_all('<Control-Key-W>', lambda event :show_w(v, licencias['textow']))
    boton_url.config(command = lambda :examinar(entry_url))
    boton_generar.config(command = lambda :generar (v, entry_desde,
            entry_intervalo,entry_cantdig,entry_ciclos,
            entry_url,logbox))

    marco_url.pack(side=tk.TOP,pady=(10,10))
    marco_url_entry.pack(side=tk.LEFT)
    label_url.pack(side=tk.TOP)
    entry_url.pack(side=tk.TOP,padx=(10,10))
    marco_url_boton.pack(side=tk.LEFT)
    boton_url.pack(side=tk.TOP,pady=(15,0),padx=(0,10))

    marco_datos.pack(side=tk.TOP)
    marco_d_labels.pack(side=tk.LEFT)
    marco_d_ingreso.pack(side=tk.LEFT)
    label_desde.pack(side=tk.TOP,anchor=tk.E,pady=(0,5))
    entry_desde.pack(side=tk.TOP,pady=(0,5))
    label_intervalo.pack(side=tk.TOP,anchor=tk.E,pady=(0,5))
    entry_intervalo.pack(side=tk.TOP,pady=(0,5))
    label_cantdig.pack(side=tk.TOP,anchor=tk.E,pady=(0,5))
    entry_cantdig.pack(side=tk.TOP,pady=(0,5))
    label_ciclos.pack(side=tk.TOP,anchor=tk.E,pady=(0,5))
    entry_ciclos.pack(side=tk.TOP,pady=(0,5))

    marco_botones.pack(side=tk.TOP,fill = tk.BOTH,pady=(10,10))
    boton_generar.pack(side=tk.RIGHT,anchor=tk.E,padx=(10,10))
    marco_log.pack(side=tk.TOP,pady=(10,10),padx=(10,10))
    logbox.pack(side=tk.LEFT, fill = tk.BOTH, expand=tk.YES)
    logbox_scrollbar.pack(side=tk.RIGHT, fill = tk.BOTH)
    logbox.config(yscrollcommand = logbox_scrollbar.set)
    logbox_scrollbar.config(command = logbox.yview)

    loguea(logbox,licencias['gplv3'])

    entry_desde.focus_set()

    v.mainloop()


muestra_ventana()
