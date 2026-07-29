$insert = @'
                <p>
                    The science behind this topic shows how interconnected climate systems are and why each element matters for people and nature across the world. Improving climate literacy, supporting evidence-based decision-making, and connecting local actions to global climate goals are all part of the broader response.
                </p>
                <p>
                    Practical solutions include reducing emissions, increasing energy efficiency, protecting natural carbon sinks such as forests and wetlands, and investing in resilient infrastructure. These actions must be supported by strong policy, community leadership, and innovation in clean technology to deliver lasting progress.
                </p>
                <p>
                    By reading and sharing accurate information, visitors can help build the public understanding needed to make better choices and encourage policymakers to act. This page is designed to deepen awareness of the issue and to highlight why climate change must remain a top priority for sustainable development, health, and economic security.
                </p>
                <p>
                    Each of these vlog posts is meant to invite readers to think beyond a single headline and to appreciate the many ways climate change interacts with our environment, economy, and communities. The more we understand the connections, the stronger our collective ability to support effective climate action and protect future generations.
                </p>
'@

Get-ChildItem -Path 'climate' -Filter 'climate-vlog*.html' | Sort-Object Name | ForEach-Object {
    $path = $_.FullName
    $text = Get-Content -Path $path -Raw
    if ($text -notmatch [regex]::Escape('The science behind this topic shows how interconnected climate systems are')) {
        $updated = [regex]::Replace($text, '(?s)(</p>\s*)(</section>)', "$1$insert$2", 1)
        if ($updated -ne $text) {
            Set-Content -Path $path -Value $updated -Encoding UTF8
        }
    }
}
