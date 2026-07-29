import glob
import re
from pathlib import Path

insert = "\n                <p>\n                    The science behind this topic shows how interconnected climate systems are and why each element matters for people and nature across the world. Improving climate literacy, supporting evidence-based decision-making, and connecting local actions to global climate goals are all part of the broader response.\n                </p>\n                <p>\n                    Practical solutions include reducing emissions, increasing energy efficiency, protecting natural carbon sinks such as forests and wetlands, and investing in resilient infrastructure. These actions must be supported by strong policy, community leadership, and innovation in clean technology to deliver lasting progress.\n                </p>\n                <p>\n                    By reading and sharing accurate information, visitors can help build the public understanding needed to make better choices and encourage policymakers to act. This page is designed to deepen awareness of the issue and to highlight why climate change must remain a top priority for sustainable development, health, and economic security.\n                </p>\n                <p>\n                    Each of these vlog posts is meant to invite readers to think beyond a single headline and to appreciate the many ways climate change interacts with our environment, economy, and communities. The more we understand the connections, the stronger our collective ability to support effective climate action and protect future generations.\n                </p>\n"
magic = 'The science behind this topic shows how interconnected climate systems are'

for path_str in sorted(glob.glob('climate/climate-vlog*.html')):
    path = Path(path_str)
    text = path.read_text(encoding='utf-8')
    if magic in text:
        continue
    match = re.search(r'(<section class="vlog-content justified">)(.*?)(</section>)', text, re.S)
    if not match:
        raise RuntimeError(f'No vlog-content section in {path}')
    before, content, after = match.groups()
    new_content = content.rstrip() + insert
    new_text = text[:match.start(2)] + new_content + text[match.end(2):]
    path.write_text(new_text, encoding='utf-8')
