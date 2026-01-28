# Compliance e Moderação

## Proteção de Dados (LGPD)

**Compromissos:**

- **Consentimento Explícito:** Usuário sabe exatamente quais dados coletamos
- **Minimização:** Coletamos apenas o necessário (perfil público + email)
- **Portabilidade:** Usuário pode exportar todos os seus dados em JSON
- **Direito ao Esquecimento:** Deletar conta remove permanentemente dados pessoais (mantém posts anonimizados)
- **Sem Venda de Dados:** Dados nunca serão compartilhados com terceiros

**Dados Coletados:**

- Email (para login)
- Nome público e bio (visível para outros)
- Estatísticas de jogo (se usuário optar por integração)
- Posts e interações públicas em comunidades

## Moderação Comunitária

**Estrutura:**

- **Auto-Moderação:** Criadores de comunidades são moderadores padrão
- **Sistema de Reports:** Usuários podem reportar posts/perfis (categorias: spam, assédio, ilegal)
- **Processo de Análise:** Reports são analisados manualmente (sem ban automático)
- **Escalação:** Casos graves são encaminhados ao administrador principal

**Código de Conduta (Básico):**

1. Proibido: discurso de ódio, assédio, conteúdo ilegal, spam
2. Incentivado: respeito, colaboração, compartilhamento de conhecimento
3. Consequências: advertência → suspensão temporária → ban permanente

## Segurança da Conta

- **Autenticação Social:** Login via Steam/Discord (Supabase OAuth)
- **Sem Senhas Armazenadas:** Delegamos auth para provedores confiáveis
- **2FA Opcional:** Pode ser implementado via Supabase no futuro
- **Sessões Seguras:** Tokens JWT com expiração

## Propriedade Intelectual

**Posicionamento:**

- **Logos de Jogos:** Uso sob Fair Use para fins informativos (catálogo de jogos)
- **Avatares/Skins Customizados:** Usuário mantém copyright, plataforma tem licença de exibição
- **Posts/Conteúdo:** Usuário é dono, mas concede licença para exibição na plataforma
