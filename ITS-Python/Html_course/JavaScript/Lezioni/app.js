console.log("node");

const arr1 = [1,2,3];
arr2 =  [...arr1]; // così si fa la swallow cospy
arr1.push(4);
console.log(arr1);
console.log(arr2);

const a = 4;
console.log(a);

const prof={
    "first name": "Roberto",
    cognome: "delisio",
    age: 48
};

console.log(prof["first name"])

const prof2 = new Object();

prof2.nome = "rob";
prof2.cognome = "del";
console.log(prof2)

class persona {
    constructor(nome = '', cognome = '') {
        this.nome = nome;
        this.cognome = cognome;
    }
}

const persona1 = new persona('bob', 'ross');
const persona2 = new persona('diddo', 'diddy');

console.log(persona1, persona2);

