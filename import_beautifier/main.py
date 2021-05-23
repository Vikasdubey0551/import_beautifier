import os
import glob


# to control the output colors
os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

class Beautify(object):
    
    def __init__(self,
                 filename=None, 
                 reverse=False, 
                 recursive=False, 
                 overwrite=False):
        self.filename = filename
        self.reverse = reverse
        self.recursive = recursive
        self.overwrite = overwrite
        if filename is None and not recursive:
            raise Exception('Choose a file or set recursive=True')
        
    def read_file(self, file):
        with open(file,'r') as f:
            data = f.readlines()
        f.close()
        return data  
    
    def write_file(self, file, data):
        with open(file, 'w') as f:
            f.write(''.join(data))
        f.close()
        
    def process_file(self, file_, data):
        
            import_lines = [i for i in data if i.startswith('import')]
            from_lines = [i for i in data if i.startswith('from')]
            code_lines = [i for i in data if not (i.startswith('import') or i.startswith('from'))]
                    
            import_lines = sorted(import_lines, key=len, reverse=self.reverse)
            from_lines = sorted(from_lines, key=len, reverse=self.reverse)
                    
            output = import_lines + from_lines + code_lines
            if self.overwrite:
                self.write_file(file_, output)
            else:
                file_ = file_.split('.')[0] + '_beautified.py'
                self.write_file(file_, output)
                    
            print(f'Beautified {style.GREEN}' + f'{file_} \u2705')
        
            
                  
    def beautify(self):
        
            if self.filename is not None:                 
                data = self.read_file(self.filename)
                self.process_file(self.filename, data)
                       
            elif self.filename is None and self.recursive:
                for file_ in glob.glob('.', recursive=True):
                    if file_.startswith('main') or file_.startswith('__init__') :
                        continue
                    data = self.read_file(file_)
                    self.process_file(file_,data)
                           

if __name__ == '__main__':
    
    beautify = Beautify('import_beautifier/test.py', overwrite=True, recursive=True)
    beautify.beautify()
