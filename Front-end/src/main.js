import api from './requisicoes_api'

class App {
    constructor() {
        this.formulario = document.getElementById('formDados')

        // Inputs
        this.ritmo = document.getElementById('ritmo')
        this.drible = document.getElementById('drible')
        this.finalizacao = document.getElementById('finalizacao')
        this.defesa = document.getElementById('defesa')
        this.passe = document.getElementById('passe')
        this.fisico = document.getElementById('fisico')
        this.goleiro = document.getElementById('goleiro')

        // Div card
        this.divCard = document.getElementById('cardFifa')

        // Posição/Overal
        this.overall = document.getElementById('overall')
        this.posicao = document.getElementById('posicao')


        // Visibilidade do card.
        this.divCard.hidden = true;

        this.registraEventos();
    }

    registraEventos() {
        this.formulario.onsubmit = event => this.RevelaPosicao(event);
    }

    async RevelaPosicao(event) {
        event.preventDefault();

        // Checa se há campos vazios!
        if (this.ritmo.value.length == 0 ||
            this.drible.value.length == 0 ||
            this.finalizacao.value.length == 0 ||
            this.defesa.value.length == 0 ||
            this.passe.value.length == 0 ||
            this.fisico.value.length == 0 ||
            this.goleiro.value.length == 0) {
            alert('campos vazios!')
            return;
        }


        try {
            // Chamando a API e passando as informações.
            const resposta = await api.get(`\/${this.ritmo.value},${this.drible.value},
            ${this.finalizacao.value},
            ${this.defesa.value},
            ${this.passe.value},
            ${this.fisico.value},
            ${this.goleiro.value}
            `);

            // Resposta obtida
            const { position, overall } = resposta.data;

            // Atribuindo valores obtidos pelo JSON
            this.overall.value = overall;
            this.posicao.value = position;

            // Renderizando a tela.
            this.renderiza();
        } catch (erro) {
            alert('Erro ao acessar a API!');

            this.renderiza();
        }
    }

    renderiza() {
        // Setando os valores ao form
        document.getElementById('valPas').textContent = ~~this.ritmo.value
        document.getElementById('valDri').textContent = ~~this.drible.value
        document.getElementById('valSho').textContent = ~~this.finalizacao.value
        document.getElementById('valDef').textContent = ~~this.defesa.value
        document.getElementById('valPac').textContent = ~~this.passe.value
        document.getElementById('valPhy').textContent = ~~this.fisico.value

        // Setando o overall e a Posição
        document.getElementById('overall').textContent = ~~this.overall.value
        document.getElementById('posicao').textContent = this.posicao.value

        // Mostrando resultado
        this.divCard.hidden = false;
    }
}

new App();