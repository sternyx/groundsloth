# groundsloth
## Setup and Manager for Responder, MITM6, and NTLMRelayx

#### groundsloth is a menu based solution for using SpiderLabs/Responder, dirkjanm/mitm6, and SecureAuthCorp/impacket. The menu utilizes tmux to decrease verbosity from responder and mitm6. NTLMRelayx is then at the foreground for any complete hash relaying that has been found. 

### Initialization

#### groundsloth can be git cloned and the requirements can be added from the _menu option 5_. 

### Flags used
#### responder: -w Start the WPAD rogue proxy server. -f This option allows you to fingerprint a host that issued an NBT-NS or LLMNR query.
#### mitm6: none
#### ntlmrelayx: -smb2support SMB Relay Server adds support for SMB2+. -socks allows you to store sessions gained from authentication relays at a SOCKS proxy.

