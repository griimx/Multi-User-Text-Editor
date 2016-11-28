### TODO: 1) Pressing enter must start search

import tkinter as tk
import tkinter.ttk as ttk
import os

class TextFindWidget(tk.Toplevel):
    def __init__(self, root, editor, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.root = root
        self.editor = editor
        self.title("Find:")
        self.transient(root)
        self.geometry("262x55+200+250")
        tk.Label(self, text="Find All:").grid(row=0, column=0, padx=1, pady=2, sticky='e')
        self.__query = tk.StringVar()
        self.__searchbar = tk.Entry(self, width=25, textvariable=self.__query)
        self.__searchbar.grid(row=0, column=1)
        self.__searchbar.focus_set()
        self.__caseinsensitive = tk.IntVar()
        tk.Checkbutton(self, text="Ignore Case", variable=self.__caseinsensitive).grid(
                row=1, column=1, sticky='e')
        tk.Button(self, text="Find All", underline=0, command=lambda: self.search(self.__query.get(),
                self.__caseinsensitive.get())).grid(row=0, column=2, padx=3, pady=2)
        self.protocol("WM_DELETE_WINDOW", self.close_find)
        #self.root.bind("<<Enter>>", self.search)

    def search(self, query, caseinsensitive):
        count = self.editor.search_for(query, caseinsensitive)
        self.__searchbar.focus_set()
        self.title("{} matches found".format(count))

    def close_find(self):
        self.editor.textpad.tag_remove("match", "1.0", "end")
        self.destroy()

class TextReplaceWidget(tk.Toplevel):
    def __init__(self, root, editor, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.root = root
        self.editor = editor
        self.title("Replace:")
        self.transient(root)
        self.geometry("307x85+200+250")
        tk.Label(self, text="Replace:").grid(row=0, column=0, padx=1, pady=2, sticky='e')
        self.__replace = tk.StringVar()
        self.__replacebar = tk.Entry(self, width=25, textvariable=self.__replace)
        self.__replacebar.grid(row=0, column=1)
        self.__replacebar.focus_set()
        tk.Label(self, text="Replace with:").grid(row=1, column=0, padx=1, pady=2, sticky='e')
        self.__replacewith = tk.StringVar()
        self.__replacewithbar = tk.Entry(self, width=25, textvariable=self.__replacewith)
        self.__replacewithbar.grid(row=1, column=1)
        self.__caseinsensitive = tk.IntVar()
        tk.Checkbutton(self, text="Ignore Case", variable=self.__caseinsensitive).grid(
                row=2, column=1, sticky='e')
        tk.Button(self, text="Find All", underline=0, command=lambda:self.editor.search_for(self.__replace.get(),
                self.__caseinsensitive.get())).grid(row=0, column=2, padx=3, pady=2, sticky="nsew")
        tk.Button(self, text="Replace All", underline=0, command=lambda: self.replace(self.__replace.get(),
                self.__replacewith.get(), self.__caseinsensitive.get())).grid(row=1, column=2, padx=3, pady=2)
        self.protocol("WM_DELETE_WINDOW", self.close_replace)
        #self.root.bind("<<Enter>>", self.search)

    def replace(self, replace, replacewith, caseinsensitive):
        count = self.editor.replace_for(replace, replacewith, caseinsensitive)
        self.__replacebar.focus_set()
        self.title("{} replaced".format(count))

    def close_replace(self):
        self.destroy()

### A notebook with close button
class Notebook(ttk.Notebook):
    def __init__(self, root):
        ttk.Notebook.__init__(self, root, style=style)
        self.root = root
        imgdir = os.path.join(os.path.dirname(__file__), 'img')
        i1 = tk.PhotoImage("img_close", file=os.path.join(imgdir, 'close.gif'))
        i2 = tk.PhotoImage("img_closeactive",
            file=os.path.join(imgdir, 'close_active.gif'))
        i3 = tk.PhotoImage("img_closepressed",
            file=os.path.join(imgdir, 'close_pressed.gif'))

        style = ttk.Style()

        style.element_create("close", "image", "img_close",
            ("active", "pressed", "!disabled", "img_closepressed"),
            ("active", "!disabled", "img_closeactive"), border=8, sticky='')

        style.layout("ButtonNotebook", [("ButtonNotebook.client", {"sticky": "nswe"})])
        style.layout("ButtonNotebook.Tab", [
            ("ButtonNotebook.tab", {"sticky": "nswe", "children":
                [("ButtonNotebook.padding", {"side": "top", "sticky": "nswe",
                                             "children":
                    [("ButtonNotebook.focus", {"side": "top", "sticky": "nswe",
                                               "children":
                        [("ButtonNotebook.label", {"side": "left", "sticky": ''}),
                         ("ButtonNotebook.close", {"side": "left", "sticky": ''})]
                    })]
                })]
            })]
        )
        self.root.bind_class("TNotebook", "<ButtonPress-1>", self.btn_press, True)
        self.root.bind_class("TNotebook", "<ButtonRelease-1>", self.btn_release)

    def btn_press(event):
        x, y, widget = event.x, event.y, event.widget
        elem = widget.identify(x, y)
        index = widget.index("@%d,%d" % (x, y))

        if "close" in elem:
            widget.state(['pressed'])
            widget.pressed_index = index

    def btn_release(event):
        x, y, widget = event.x, event.y, event.widget

        if not widget.instate(['pressed']):
            return

        elem =  widget.identify(x, y)
        index = widget.index("@%d,%d" % (x, y))

        if "close" in elem and widget.pressed_index == index:
            widget.forget(index)
            widget.event_generate("<<NotebookClosedTab>>")

        widget.state(["!pressed"])
        widget.pressed_index = None

class Go_Online(tk.Toplevel):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.root = root
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"




        self.Label1.place(relx=0.18, rely=0.13, height=21, width=184)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background=_bgcolor)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Enter code for collaboration''')

        self.Label3.place(relx=0.33, rely=0.37, height=21, width=94)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#2333f5")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")

        self.Button1.place(relx=0.36, rely=0.62, height=24, width=72)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background=_bgcolor)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Collaborate''')

class Host_Online(tk.Toplevel):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.root = root
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"




        self.Label1.place(relx=0.18, rely=0.13, height=21, width=184)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background=_bgcolor)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Enter code for collaboration''')

        self.Label3.place(relx=0.33, rely=0.37, height=21, width=94)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#2333f5")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''12gf''')

        self.Label2.place(relx=0.17, rely=0.59, height=21, width=199)
        self.Label2.configure(background=_bgcolor)
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Share this code to start collaboration''')
