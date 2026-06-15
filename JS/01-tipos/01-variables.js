// En JavaScript, las variables son contenedores que almacenan datos. Se pueden declarar utilizando las palabras clave "var", "let" o "const". La diferencia entre estas palabras clave radica en el alcance y la mutabilidad de las variables que crean.
// "var" tiene un alcance de función y permite la redeclaración, 
// mientras que "let" tiene un alcance de bloque y no permite la redeclaración.
// "const" también tiene un alcance de bloque, pero además no permite la reasignación de su valor una vez que ha sido inicializada.
let nombre= "Hola mundo!";

let NombreCompleto;//Esto es un ejemplo de nombrado de variables llamado UpperCamelCase,
// donde la primera letra de cada palabra está en mayúscula.
let nombreCompleto;//Esto es un ejemplo de nombrado de variables llamado camelCase,
// donde la primera letra de la palabra está en minúscula y la primera letra de cada palabra subsiguiente está en mayúscula.
let nombre_completo;//Esto es un ejemplo de nombrado de variables llamado snake_case,
// donde las palabras están separadas por guiones bajos y todas las letras están en minúscula.

console.log(nombre);

let apellido;//Puedes definir varias variables en un mismo let, separandolas por comas.
// Pero no es recomendable hacerlo, ya que puede dificultar la lectura del código y generar confusión. Es mejor definir cada variable en una línea separada para mejorar la legibilidad y el mantenimiento del código.
apellido = "Hernandez";//A una variable ya creada se le puede asignar un valor posteriormente,
// incluso si no se le asignó un valor en el momento de su declaración.
// Esto es posible gracias a la flexibilidad de JavaScript, que permite la asignación de valores a variables en cualquier momento después de su declaración.