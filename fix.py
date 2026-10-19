import re, glob

def fix(src):
    def r(m):
        parts = [m.group(1)]
        for mm in re.finditer(r"'([^']*)'", m.group(2) or ''):
            parts.append(mm.group(1))
        return "example:'" + "<br><br>".join(parts) + "'"
    src = re.sub(r"example:'([^']*)'((?:\s*,\s*'[^']*')*)", r, src)
    src = re.sub(r"(example:'[^']*')\]", r"\1", src)
    return src

for path in sorted(glob.glob('lectures*.js')):
    try:
        with open(path, encoding='utf-8') as f:
            src = f.read()
        src = fix(src)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(src)
        print('ok:', path)
    except Exception as e:
        print('ошибка в', path, ':', e)
print('Готово.')

