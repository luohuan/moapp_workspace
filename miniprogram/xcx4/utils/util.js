module.exports={jsonToUrlParams:e=>{let n="";for(var o in e||{}){n+="&"+o+"="+encodeURIComponent(e[o])}return n.length==0?"":n.slice(1,n.length)}};