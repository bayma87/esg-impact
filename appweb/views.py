from django.shortcuts import render, redirect

from .forms import ContactMessageForm


QUESTIONS = [
    {'id': 'e1', 'pillar': 'Ambiental', 'text': 'A empresa monitora mensamente o consumo de energia e água?', 'weight': 1},
    {'id': 'e2', 'pillar': 'Ambiental', 'text': 'Há gestão de resíduos e percentual de reciclagem?', 'weight': 1},
    {'id': 'e3', 'pillar': 'Ambiental', 'text': 'Existem políticas para reduzir emissões e desperdícios?', 'weight': 1},
    {'id': 's1', 'pillar': 'Social', 'text': 'A empresa possui políticas de diversidade, inclusão e bem-estar?', 'weight': 1},
    {'id': 's2', 'pillar': 'Social', 'text': 'Há treinamento e capacitação de colaboradores com frequência?', 'weight': 1},
    {'id': 's3', 'pillar': 'Social', 'text': 'A organização acompanha a segurança, saúde e engajamento da equipe?', 'weight': 1},
    {'id': 'g1', 'pillar': 'Governança', 'text': 'Existe código de ética e canais de denúncia claros?', 'weight': 1},
    {'id': 'g2', 'pillar': 'Governança', 'text': 'A empresa define metas de sustentabilidade e acompanhamento de risco?', 'weight': 1},
    {'id': 'g3', 'pillar': 'Governança', 'text': 'Há transparência e prestação de contas para a liderança e stakeholders?', 'weight': 1},
]

PILLAR_ORDER = ['Ambiental', 'Social', 'Governança']


def calculate_scores(answer_map):
    scores = {pillar: 0 for pillar in PILLAR_ORDER}
    totals = {pillar: 0 for pillar in PILLAR_ORDER}

    for question in QUESTIONS:
        response = int(answer_map.get(question['id'], 0))
        scores[question['pillar']] += response
        totals[question['pillar']] += 2

    pillar_scores = {}
    for pillar in PILLAR_ORDER:
        if totals[pillar] == 0:
            pillar_scores[pillar] = 0
        else:
            pillar_scores[pillar] = round((scores[pillar] / totals[pillar]) * 100)

    overall_score = round(sum(pillar_scores.values()) / len(PILLAR_ORDER))
    weakest_pillar = min(pillar_scores, key=pillar_scores.get)

    return pillar_scores, overall_score, weakest_pillar


def get_recommendations(weakest_pillar):
    recommendations = {
        'Ambiental': [
            'Implementar indicadores mensais de consumo de energia, água e resíduos.',
            'Definir plano de redução de desperdícios e aumentar a reciclagem.',
            'Estabelecer metas de eficiência ambiental para produção e logística.',
        ],
        'Social': [
            'Reforçar políticas de inclusão, bem-estar e capacitação dos colaboradores.',
            'Implementar diagnóstico de clima organizacional e ações de engajamento.',
            'Padronizar treinamentos em saúde, segurança e desenvolvimento profissional.',
        ],
        'Governança': [
            'Atualizar código de ética, políticas internas e canais de denúncia.',
            'Estabelecer KPIs de sustentabilidade para a liderança e reuniões do conselho.',
            'Criar rotina de governança ESG com indicadores e rastreio de riscos.',
        ],
    }
    return recommendations.get(weakest_pillar, recommendations['Governança'])


def home(request):
    return render(request, 'appweb/home.html')


def quem_somos(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'appweb/quem_somos.html', {
                'form': ContactMessageForm(),
                'success_message': 'Pergunta enviada com sucesso! Nossa equipe responderá em breve.'
            })
    else:
        form = ContactMessageForm()

    return render(request, 'appweb/quem_somos.html', {'form': form})
