import glob
import re
from pathlib import Path

for path_str in sorted(glob.glob('climate/climate-vlog*.html')):
    path = Path(path_str)
    text = path.read_text(encoding='utf-8')
    match = re.search(r'<section class="vlog-content justified">(.*?)</section>', text, re.S)
    content = match.group(1) if match else ''
    plain = re.sub(r'<.*?>', '', content)
    words = len(re.findall(r'\w+', plain))
    print(f'{path.name},{words}')
