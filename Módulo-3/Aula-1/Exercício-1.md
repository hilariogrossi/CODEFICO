Diagrama de Minimundo para Aplicação de Mensagens (Tipo whatsapp)

Usuários
---------
ID (PK)
Nome
Telefone
FotoPerfil

Conversas
---------
ID (PK)
Nome (Opcional, para conversas em grupo)
Tipo (Pessoal ou Grupo)

Participantes
-------------
ID (PK)
ConversaID (FK)
UsuarioID (FK)

Mensagens
---------
ID (PK)
ConversaID (FK)
RemetenteID (FK)
Conteúdo
DataHora

StatusMensagem
--------------
ID (PK)
MensagemID (FK)
UsuarioID (FK)
Status (Enviada, Recebida, Visualizada)
DataHoraStatus
