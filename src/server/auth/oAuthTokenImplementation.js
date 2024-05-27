/* 
Web Based Auth System ---- 

PLEASE DON'T USE THIS FOR SYSTEMS USED BY ACTUAL PEOPLE I BEG YOU
IT'S NOT SECURE
YOU ARE GOING TO GET HACKED
I'M SO SORRY
*/

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
  

function GetClientOauthToken(token, client) {
    console.log("client '" + client + "' sent token '" + token + "'")
    
    //Decoding Token
    decodedToken = atob(token)
    console.log("")
    console.log("Decoded token is '" + decodedToken + "'")

}



GetClientOauthToken("Q2xpZW50UlRva2VuQXV0aFJlc3BvbnNlLURTQ01MUw==", "I'm Special")