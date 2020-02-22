var flip = function (dataArray) {
  var a = dataArray;
  for(var i = 0; i < a; i++) {
    var b = Math.random(0,1);
    var c = Math.round(b);
    var d;
    if(c = 0) {
      a[i] = a[i];
    }
    else {
      a[i] = false;
    }
  }
  return a;
}
