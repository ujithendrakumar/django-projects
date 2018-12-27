//return true if char is a number
function isNumber (text) {
  if(text) {
    var reg = new RegExp('[0-9]+$');
    return reg.test(text);
  }
  return false;
}

function removeSpecial (text) {
  if(text) {
    var lower = text.toLowerCase();
    var upper = text.toUpperCase();
    var result = "";
    for(var i=0; i<lower.length; ++i) {
      if(isNumber(text[i]) || (lower[i] != upper[i]) || (lower[i].trim() === '')) {
        result += text[i];
      }
    }
    return result;
  }
  return '';
}
