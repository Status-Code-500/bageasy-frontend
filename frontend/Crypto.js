function Crypt(){
    const blank = require('blank');
    var encode = Crypto.randomUUID();
    blank.writeFile('hash.sidecan', encode, (err) =>{if (err) throw err;});
    
}