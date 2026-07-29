import os
import re

root = 'climate'

content_map = {
    'Greenhouse Gas Emissions & Sources': (
        "Greenhouse gas emissions are the core cause of modern climate change, and understanding their sources is essential for effective action. "
        "These gases include carbon dioxide, methane, nitrous oxide, and fluorinated gases, each of which traps heat differently in the atmosphere. "
        "Major emission sources are electricity and heat production, industrial processes, transportation, buildings, and agriculture. "
        "The continued use of coal, oil, and gas releases enormous quantities of carbon dioxide, while livestock and rice paddies contribute methane and nitrous oxide. "
        "Even land-use changes such as deforestation reduce the planet's ability to absorb carbon, which makes emissions worse. "
        "By identifying where emissions come from, communities and policymakers can prioritize clean energy, sustainable farming, and better waste management to bend the emissions curve downward."
    ),
    'Carbon Dioxide (CO₂) Concentration Trends': (
        "Carbon dioxide concentration trends offer one of the clearest records of human influence on climate. "
        "Since the Industrial Revolution, atmospheric CO₂ has climbed from about 280 parts per million to more than 420 ppm, a level not observed for hundreds of thousands of years. "
        "Long-term measurements from observatories such as Mauna Loa reveal not only a steady upward trend, but also seasonal oscillations caused by plant growth cycles. "
        "The persistence of CO₂ in the atmosphere means that each additional ton of emissions contributes to warming for centuries. "
        "Tracking these trends helps scientists project future warming and reinforces the urgency of cutting emissions quickly to avoid dangerous climate impacts."
    ),
    'Methane (CH₄) and Its Climate Impact': (
        "Methane is a potent greenhouse gas that plays a major role in short-term climate warming. "
        "Although it remains in the atmosphere for a shorter period than carbon dioxide, methane is more than 25 times stronger at trapping heat over a 100-year timeframe and more than 80 times stronger over 20 years. "
        "It is emitted during fossil fuel extraction, from livestock digestion, landfills, and wetlands. "
        "Because methane is both powerful and relatively short-lived, cutting it can slow warming quickly and provide valuable near-term benefits. "
        "Mitigating methane emissions is therefore a high-leverage climate solution, especially when paired with longer-term efforts to reduce carbon dioxide."
    ),
    'The Greenhouse Effect Explained': (
        "The greenhouse effect is a natural process that keeps Earth warm enough to support life, but human activities have amplified it. "
        "Sunlight reaches the planet and warms the surface, and greenhouse gases trap some of the outgoing heat, preventing it from escaping too quickly. "
        "Without this process, Earth would be far colder, but excess greenhouse gases create an enhanced greenhouse effect that raises global temperatures. "
        "This imbalance alters weather, ocean circulation, and the water cycle, making the climate system more volatile. "
        "Understanding the greenhouse effect helps explain why reducing emissions is essential for stabilizing the climate and protecting ecosystems."
    ),
    'Global Temperature Rise & Historical Records': (
        "Global temperature records show that the recent rise in Earth’s average temperature is unprecedented in human history. "
        "Instrumental data from the past 150 years indicate that each of the last four decades has been warmer than the one before, with the last decade being the warmest on record. "
        "Scientists also use proxy records such as ice cores, tree rings, and sediment layers to compare modern warming with natural variability over centuries and millennia. "
        "These historical records demonstrate that the speed and magnitude of current warming are far outside normal patterns. "
        "The implications are serious: more heat waves, shifting rainfall patterns, melting ice, and a higher likelihood of crossing dangerous climate thresholds."
    ),
    'IPCC Reports & Climate Science': (
        "IPCC reports represent the most comprehensive international assessments of climate science and policy. "
        "Produced by hundreds of scientists from around the world, these reports synthesize observations, model results, and impacts studies to inform decision makers. "
        "They describe how warming is already affecting ecosystems, agriculture, water resources, and human health, and they quantify the risks of different emissions pathways. "
        "The reports also outline mitigation and adaptation options, emphasizing that rapid, deep emissions reductions are needed to limit warming. "
        "Following IPCC findings helps governments align national climate plans with scientific evidence and keep the world on a safer trajectory."
    ),
    'Paris Agreement & International Climate Policy': (
        "The Paris Agreement is a global climate accord designed to keep warming well below 2°C above pre-industrial levels, and pursue efforts to limit it to 1.5°C. "
        "Signed by almost every country, the agreement relies on nationally determined contributions, peer review, and regular updates. "
        "It recognizes that developed countries should lead but that all nations must build resilience and reduce emissions in ways that are fair and just. "
        "International climate policy also addresses finance for clean energy, technology transfer, and support for vulnerable communities. "
        "Strengthening action under the Paris framework is essential if the world is to avoid the worst consequences of climate change and to support a just transition for all."
    ),
    'Carbon Footprint & Personal Impact': (
        "Every person and organization has a carbon footprint, which is the total amount of greenhouse gases emitted directly and indirectly. "
        "Transport, energy use, diet, consumption, and waste all contribute, and small choices add up when repeated across millions of people. "
        "Individuals can reduce their footprint by using public transit, eating more plant-based foods, improving home energy efficiency, and choosing renewable electricity. "
        "Businesses and governments can support these changes through sustainable infrastructure, cleaner supply chains, and green procurement. "
        "Understanding personal impact empowers people to make meaningful climate-friendly choices and to advocate for systemic solutions."
    ),
    'Fossil Fuels & the Energy Transition': (
        "Fossil fuels such as coal, oil, and natural gas have powered industrial development, but they are also the largest source of carbon dioxide emissions. "
        "A successful energy transition shifts the world toward renewable resources like wind, solar, hydro, and geothermal, while phasing out high-emitting fuels. "
        "This transition requires modernizing grids, investing in storage, improving energy efficiency, and supporting workers in affected industries. "
        "Moving away from fossil fuels reduces air pollution, strengthens energy security, and helps economies become more resilient. "
        "The pace of the transition will determine whether global warming can be limited and whether future generations inherit a safer climate."
    ),
    'Deforestation & Land Use Change': (
        "Deforestation and land-use change are major drivers of carbon emissions and biodiversity loss. "
        "When forests are cleared for agriculture, logging, or development, the carbon stored in trees and soil is released into the atmosphere. "
        "Healthy forests also regulate rainfall, protect watersheds, and provide habitat for wildlife and local communities. "
        "Protecting forests and restoring degraded land are therefore critical climate strategies that also support livelihoods and nature. "
        "By changing how land is used, society can preserve important carbon sinks and reduce the combined impact of human activity on climate systems."
    ),
    'Melting Glaciers & Polar Ice Caps': (
        "Melting glaciers and polar ice caps are among the most visible signs of climate change. "
        "As global temperatures rise, mountain glaciers retreat and ice sheets in Greenland and Antarctica lose mass. "
        "This melting contributes to sea level rise, alters freshwater supplies for millions of people, and changes the reflectivity of the planet's surface. "
        "When ice disappears, darker land or ocean absorbs more heat, creating a feedback loop that accelerates warming. "
        "Monitoring these cryosphere changes is vital because they serve as a warning that the climate is changing faster than many ecosystems can adapt."
    ),
    'Sea Level Rise & Coastal Impacts': (
        "Sea level rise threatens coastal communities, ecosystems, and infrastructure around the world. "
        "Rising seas are driven by thermal expansion of warming oceans, glacier melt, and ice sheet loss. "
        "Even modest increases can worsen storm surges, accelerate erosion, and flood low-lying land. "
        "Many cities, agricultural areas, and fisheries depend on coastlines that are now at growing risk. "
        "Planning for coastal impacts means combining emissions reductions with adaptation measures such as building resilient defenses, preserving wetlands, and relocating vulnerable populations where needed."
    ),
    'Extreme Weather Events (Heatwaves, Storms, Floods)': (
        "Climate change is increasing the frequency and intensity of extreme weather events, including heatwaves, storms, and floods. "
        "Warmer air holds more moisture, which can fuel heavier rainfall and more powerful storms. "
        "Heatwaves become more severe and longer, placing stress on people, agriculture, and energy systems. "
        "Flooding from intense rain and rising seas damages property and disrupts communities, while stronger storms can destroy infrastructure. "
        "Understanding these risks helps societies prepare and respond more effectively to the changing nature of weather hazards."
    ),
    'Climate Feedback Loops (Albedo, Permafrost)': (
        "Climate feedback loops can amplify warming by reinforcing the processes that cause it. "
        "One important example is albedo, the reflectivity of Earth's surface: ice and snow reflect sunlight, but when they melt, darker surfaces absorb more heat. "
        "Another key feedback involves permafrost, which stores large amounts of carbon and methane. "
        "As permafrost thaws, it releases these greenhouse gases, which can further warm the atmosphere and increase thawing. "
        "Recognizing these feedbacks underscores why limiting warming early is so important to avoid runaway changes in the climate system."
    ),
    'Ocean Warming & Acidification': (
        "Ocean warming and acidification are major consequences of greenhouse gas emissions. "
        "The oceans absorb most of the excess heat trapped by greenhouse gases, which changes marine habitats and circulation patterns. "
        "At the same time, seawater absorbs carbon dioxide and becomes more acidic, which threatens shell-forming organisms such as corals, mollusks, and plankton. "
        "These changes ripple through marine food webs and impact fisheries, tourism, and coastal livelihoods. "
        "Protecting the oceans requires both reducing emissions and managing coastal ecosystems more sustainably."
    ),
    'Climate Refugees & Environmental Migration': (
        "Climate change is already forcing people to move when their homes and livelihoods become unsafe. "
        "Rising seas, drought, extreme storms, and changing agricultural conditions can displace communities, especially in vulnerable regions. "
        "The term climate refugees highlights the human cost of environmental disruption and the need for fair policies to support those who must relocate. "
        "Planning for migration includes improving resilience, providing humanitarian assistance, and creating legal pathways for people affected by climate-related loss and damage. "
        "Addressing the root causes of displacement through climate action is essential to reducing future migration pressures."
    ),
    'Climate Mitigation Strategies': (
        "Climate mitigation strategies are the actions taken to reduce greenhouse gas emissions and slow warming. "
        "They include transitioning to clean energy, increasing energy efficiency, improving transportation systems, and stopping deforestation. "
        "Mitigation also means investing in low-carbon technologies, sustainable agriculture, and responsible consumption patterns. "
        "Policies such as carbon pricing, regulations, and incentives can help scale these changes across economies. "
        "Strong mitigation efforts today lower the risk of future climate impacts and make adaptation easier for communities worldwide."
    ),
    'Climate Adaptation & Resilience Planning': (
        "Climate adaptation and resilience planning help communities prepare for the impacts of warming already underway. "
        "This includes strengthening infrastructure, protecting water resources, improving agricultural methods, and creating early warning systems. "
        "Resilience means designing systems that can absorb shocks and recover quickly after extreme events. "
        "Adaptation planning should prioritize the most vulnerable people and ecosystems to ensure equity and durability. "
        "By combining mitigation and adaptation, societies can reduce harm and build a safer future even as the climate changes."
    ),
    'Carbon Capture, Utilization & Storage (CCUS)': (
        "Carbon capture, utilization, and storage (CCUS) technologies aim to remove carbon dioxide from energy and industrial facilities or directly from the air. "
        "Captured CO₂ can be stored underground in geological formations or used to produce materials, fuels, and chemicals. "
        "CCUS is seen as a complementary tool alongside emissions reductions, especially for sectors that are hard to decarbonize. "
        "However, it must be deployed responsibly and at scale to deliver meaningful climate benefits. "
        "The future of CCUS depends on policy support, investment, and careful management of environmental risks."
    ),
    'Renewable Energy & Decarbonization': (
        "Renewable energy and decarbonization are central to efforts to reduce climate change risk. "
        "Solar, wind, hydro, and geothermal power produce electricity without direct carbon emissions and are increasingly cost-competitive. "
        "Decarbonization also involves electrifying transport, heating, and industry and using clean fuels when electricity is not available. "
        "Scaling renewables requires modern grids, energy storage, and smart demand management. "
        "The transition to renewables can create jobs, improve air quality, and help countries meet their climate targets sustainably."
    ),
    'Climate Justice & Equity': (
        "Climate justice and equity focus on the fact that the people least responsible for emissions often suffer the worst impacts. "
        "Vulnerable communities, low-income countries, and marginalized groups frequently face greater exposure to climate hazards and have fewer resources to adapt. "
        "Fair climate action means supporting these populations with finance, technology, and capacity building. "
        "It also means including diverse voices in decision making and ensuring a just transition for workers and communities affected by the energy shift. "
        "Centering justice in climate policy helps build solutions that are effective, inclusive, and sustainable over the long term."
    ),
    'Climate Modeling & Future Predictions': (
        "Climate modeling and future predictions allow scientists to explore how different emissions pathways may affect the planet. "
        "Models combine physics, chemistry, and observations to simulate atmospheric, oceanic, and land processes. "
        "They are used to estimate temperature changes, precipitation shifts, sea level rise, and extreme event frequency. "
        "While models have uncertainties, they consistently show that higher emissions lead to more severe climate impacts. "
        "This information is crucial for planning and policymaking, because it helps societies prepare for possible futures and choose safer courses of action."
    ),
    'Agriculture & Food Security Under Climate Change': (
        "Agriculture and food security are deeply affected by climate change, as shifting rainfall, heat stress, and pests alter growing conditions. "
        "Crop yields may decline in many regions, especially where farmers already face water scarcity and poor soils. "
        "Climate-smart agriculture practices such as crop diversification, improved irrigation, and soil conservation can help maintain productivity. "
        "At the same time, reducing emissions from farming and food systems is important, because agriculture is a significant source of methane and nitrous oxide. "
        "Protecting food security under climate change requires adapting agriculture while supporting smallholder farmers and sustainable diets."
    ),
    'Biodiversity Loss Linked to Climate Change': (
        "Climate change is causing biodiversity loss by altering habitats, ecosystems, and species interactions. "
        "Rising temperatures, changing precipitation patterns, ocean warming, and acidification all threaten plants and animals. "
        "Many species must move, adapt, or face greater risk of extinction as their environments change too rapidly. "
        "Protecting biodiversity depends on reducing emissions and conserving critical ecosystems such as forests, wetlands, and coral reefs. "
        "Healthy biodiversity also strengthens climate resilience, because intact ecosystems are better able to buffer against extreme events and support human well-being."
    ),
    'Net Zero Targets & Corporate Commitments': (
        "Net zero targets and corporate commitments are important signals that governments and businesses are aiming to balance emissions and removals. "
        "Achieving net zero means reducing emissions as much as possible and offsetting any remaining emissions with credible carbon removal. "
        "Companies and countries are adopting pledges, but their credibility depends on transparent plans, science-based targets, and near-term action. "
        "Net zero frameworks should also avoid relying too heavily on unproven technologies and instead prioritize real emissions cuts. "
        "When implemented responsibly, net zero commitments can drive innovation and help keep global warming within safer limits."
    ),
}

for filename in sorted(os.listdir(root)):
    if not filename.startswith('climate-vlog-') or not filename.endswith('.html'):
        continue
    path = os.path.join(root, filename)
    text = open(path, encoding='utf-8').read()
    title_match = re.search(r'<h1>(.*?)</h1>', text, re.S)
    if not title_match:
        raise RuntimeError(f'No title found in {filename}')
    title = title_match.group(1).strip()
    if title not in content_map:
        raise RuntimeError(f'No content defined for title: {title} in {filename}')
    body = content_map[title]
    body_paragraphs = body.split('  ')
    new_content = '\n'.join('                <p>\n                    ' + paragraph + '\n                </p>' for paragraph in body_paragraphs)
    new_section = '<section class="vlog-content justified">\n                \n' + new_content + '\n                \n                </section>'
    updated = re.sub(r'<section class="vlog-content justified">.*?</section>', new_section, text, flags=re.S)
    if updated == text:
        raise RuntimeError(f'Failed to replace content in {filename}')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(updated)
    word_count = len(re.findall(r"\b[\w']+\b", re.sub(r'<[^>]+>', ' ', ''.join(body_paragraphs))))
    print(f'{filename}: {word_count}')
