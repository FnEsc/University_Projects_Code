Array.prototype.contains=function(b){var a=this.length;while(a--){if(this[a]===b){return true;}}return false;};function getNewTitle(n,h,d){if(isExporting){return h;}var l=11;var m=Math.floor(n/d);var g=Math.floor(m/l);if(g>=10){g-=2;}else{if(g>=2){g-=1;}}var b="";var a="<br/>";var b="";var k="";var f=Math.ceil(h.length/g);if(f>1){for(var c=1;c<=f;c++){if(c==1){b+=h.substring(0,g)+a;k=h.substring(g);}else{var i=0;var e=g;if(k.length>g){b+=k.substring(i,e)+a;k=k.substring(e);}else{if(k.length>0){b+=k.substring(i);}}}}}else{b=h;}return b;}var HighChart={ChartDataFormate:{FormateNOGroupData:function(d){var b=[];var a=[];for(var c=0;c<d.length;c++){b.push(d[c].name||"");a.push([d[c].name,d[c].value||0]);}return{category:b,data:a};},FormatGroupData:function(e){var l=new Array();var b=new Array();var f=new Array();for(var g=0;g<e.length;g++){if(!l.contains(e[g].name)){l.push(e[g].name);}if(!b.contains(e[g].group)){b.push(e[g].group);}}for(var g=0;g<b.length;g++){var a={};var h=new Array();for(var d=0;d<e.length;d++){for(var c=0;c<l.length;c++){if(b[g]==e[d].group&&e[d].name==l[c]){h.push(e[d].value);}}}a={name:b[g],data:h,dataLabels:{enabled:true}};f.push(a);}return{category:l,series:f};}},ChartOptionTemplates:{Pie:function(e,h,g){var f=HighChart.ChartDataFormate.FormateNOGroupData(e);var d=false;for(var b=0;b<f.category.length;b++){if(f.category[b].length>10){d=true;}}var a="";if(g){a="50%";}var c={chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:false},credits:{enabled:false},exporting:{enabled:false},colors:["#54C7FC","#FFB54D","#FF7466","#44DB5E","#4D9FFF","#FFD300","#22b5c3","#a3be57","#ff9c9c","#48cfef","#25bf6e","#ea5f35","#7e85e0","#f2bd7c","#bbbbba","#7257a2"],title:{text:""},tooltip:{formatter:function(){var i=this.y;if(h){i=this.y+"%";}return"<b>"+this.point.name+"</b>："+i;},useHTML:true,percentageDecimals:1,style:{fontFamily:"Microsoft YaHei"}},legend:{itemStyle:{fontWeight:"normal",fontFamily:"Microsoft YaHei"}},plotOptions:{pie:{allowPointSelect:true,cursor:"pointer",dataLabels:{enabled:true,style:{fontSize:"13px",fontWeight:"normal","font-family":"Microsoft YaHei"},formatter:function(){var j=this.y;if(h){j=this.y+"%";}if(d){return j;}var i=this.point.name;if(i.length>10){i=i.substr(0,10)+"... ";}return i+": "+j;}},showInLegend:d}},series:[{type:"pie",name:"",data:f.data,innerSize:a}]};return c;},Bars:function(g,k,b,c){var l="column";var d=false;if(k==3){l="line";}else{if(k==4){l="bar";}else{if(k==5){d=true;l="line";}}}var a=["#33a3dc","#76c0ec","#95dc7c","#cce863","#fff500","#fca000","#22b5c3","#a3be57","#ff9c9c","#48cfef","#25bf6e","#ea5f35","#7e85e0","#f2bd7c","#bbbbba","#7257a2"];var m=HighChart.ChartDataFormate.FormatGroupData(g,b);var e=m.series.length>1;var j="";var f=false;if(c==1){f=false;}else{if(e&&m.category.length>4){f=true;}}if(e&&f){if(b){j="percent";}else{j="normal";}}if(j){var i=m.series.length;if(i<a.length){a=a.slice(0,i);a=a.reverse();}if(i==2){a=["#fca000","#33a3dc"];}}var h={chart:{polar:d,type:l},legend:{enabled:e,itemStyle:{fontWeight:"normal",fontFamily:"Microsoft YaHei"},labelFormatter:function(){if(this.name.length>12){return this.name.substr(0,12)+"...";}else{return this.name;}}},title:{text:""},credits:{enabled:false},exporting:{enabled:false},colors:a,xAxis:{categories:m.category,labels:{formatter:function(){if(j){return getNewTitle(this.axis.width,this.value,m.category.length);}else{return this.value;}},useHTML:j?true:false}},yAxis:{lineWidth:1,gridLineWidth:0,title:{text:""}},tooltip:{formatter:function(){var o=this.y;if(b){o=this.y+"%";}if(e){return"<b>"+this.series.name+"</b>："+o;}else{return"<b>"+this.x+"</b>："+o;}},useHTML:true,percentageDecimals:1,style:{fontFamily:"Microsoft YaHei"}},plotOptions:{column:{pointPadding:0.2,borderWidth:0,stacking:j,dataLabels:{style:{fontSize:"13px",fontWeight:"normal","font-family":"Microsoft YaHei"},formatter:function(){var o=this.y;if(o==0&&j){return"";}if(b){o=this.y+"%";}return o;}}},bar:{pointPadding:0.2,borderWidth:0,stacking:j,dataLabels:{style:{fontSize:"13px",fontWeight:"normal","font-family":"Microsoft YaHei"},formatter:function(){var o=this.y;if(o==0&&j){return"";}if(b){o=this.y+"%";}return o;}}},line:{dataLabels:{enabled:true,style:{fontSize:"13px",fontWeight:"normal","font-family":"Microsoft YaHei"},formatter:function(){var o=this.y;if(b){o=Highcharts.numberFormat(this.y,0)+"%";}return o;}}},series:{minPointLength:6}},series:m.series};if(k==5){var n={pane:{size:"80%"},xAxis:{categories:m.category,tickmarkPlacement:"on",lineWidth:0},yAxis:{gridLineInterpolation:"polygon",lineWidth:0,min:0}};return $.extend({},h,n);}return h;}},RenderChart:function(b,a){a.highcharts(b);}};var divarray=new Array();function initChart(){if(!divDataIds){return;}var b=divDataIds.split(",");for(var a=0;a<b.length;a++){divarray.push(document.getElementById(b[a]));}$.each(divarray,function(){$(this).find("li").click(function(){var i=$(this).parent().parent();var g=i.next().next();var h=getTable(i.prev());renderChart(h,i,g,this);});var f=$(this);var c=$(this).attr("type");if(c!="0"&&c!="1"){return true;}var d=getTable($(this).prev());var e=d.rows[0];e.cells[0].parentTable=e.cells[1].parentTable=d;e.cells[0].onclick=e.cells[1].onclick=function(){var h=this.getElementsByTagName("img")[0];if(h){if(h.src.toLowerCase().indexOf("arrownone.gif")>-1){h.src="/images/wjx/viewstat/arrowdown.gif";}else{if(h.src.toLowerCase().indexOf("arrowdown.gif")>-1){h.src="/images/wjx/viewstat/arrowup.gif";h.alt="↑";}else{h.src="/images/wjx/viewstat/arrowdown.gif";h.alt="↓";}}}if(this.cellIndex==0){d.sortType=0;}else{var j=d.sortType;if(!j){j=1;}else{if(j==1){j=2;}else{j=1;}}d.sortType=j;}var i=c=="0";sortTable(d.tBodies[0],this.cellIndex,true,i);if(f[0].lastObj){var g=f[0].lastObj;f[0].lastObj=null;$(g).trigger("click");}};});}function saveChart(f){var b=$(f).parent().prev();var a=b.highcharts();var e=b.width();var d="image/png";if(!$.browser){a.exportChart({type:d,scale:1});return;}var c=$.browser.msie&&($.browser.version=="6.0"||$.browser.version=="7.0"||$.browser.version=="8.0"||$.browser.version=="9.0");if($.browser.safari||$.browser.opera){c=true;}if(c){a.exportChart({type:d,scale:1});return;}a.exportChartLocal({type:d,scale:1});}function printChart(c){var b=$(c).parent().prev();var a=b.highcharts();a.print();}function enlargeChart(d,c){var b=$(d).parent().prev();if(c){b.width(b.width()*1.1);b.height(b.height()*1.1);}else{b.width(b.width()/1.1);b.height(b.height()/1.1);}var a=b.highcharts();a.reflow();}function daozhiChart(d){var a=$(d).parent().prev();var e=a.prev().prev();var c=a[0].tableData;if(!c){c=getTable(e.prev());}else{e=a[0].divResultCss;}c.daoZhi=!c.daoZhi;if(e[0].lastObj){var b=e[0].lastObj;e[0].lastObj=null;$(b).trigger("click");}}function percentChart(k){var b=$(k).parent().prev();var a=b.prev().prev();var d=b[0].tableData;if(!d){d=getTable(a.prev());}else{a=b[0].divResultCss;}d.notPercent=!d.notPercent;k.innerHTML=k.innerHTML=="数值"?"百分比":"数值";var o=a.attr("type");if(o=="3"||o=="4"){var p=d.rows;var m=p.length;for(var l=1;l<m;l++){var r=p[l].cells;var q=r.length;if(o=="4"){q=q-1;}for(var g=1;g<q;g++){var c=$(r[g]).text();if(!r[g].dval){var h=c.split("(");var f=h[0];var n=h[1].replace(")","").replace("[详细]","");r[g].dval=f;r[g].dpercent=n;}if(d.notPercent){r[g].innerHTML=r[g].dval;}else{r[g].innerHTML=r[g].dpercent;}}}}if(a[0].lastObj){var e=a[0].lastObj;a[0].lastObj=null;$(e).trigger("click");}}function renderChart(f,w,r,c){var m=$(c).attr("index");var e=window.location.href.indexOf("/mobile/")>-1;if(m=="0"){f.removeEmpty=f.removeEmpty?false:true;var D=f.removeEmpty?"显示零数据":"隐藏零数据";if(e){D=D.replace("数据","");}$(c).find("a")[0].innerHTML=D;var p=f.rows;for(A=1;A<p.length-1;A++){var F=p[A].cells[1].innerHTML;if(F=="0"){p[A].style.display=f.removeEmpty?"none":"";}}if(w[0].lastObj){var k=w[0].lastObj;w[0].lastObj=null;$(k).trigger("click");}return;}else{if(m=="-1"){var z=!w.hideTable;$(f).toggle();$(c).toggleClass("liSelect");return;}}if(w[0].lastObj==c&&r.is(":visible")){r.hide();r.next().hide();$(c).removeClass("liSelect");w[0].lastObj=null;return;}else{if(w[0].lastObj){$(w[0].lastObj).removeClass("liSelect");}}w[0].lastObj=c;$(w[0].lastObj).addClass("liSelect");var s=new Array();var a=!f.notPercent;var t=f.rows;var B=t.length;var h=w.attr("type");if(h=="1"){a=false;}else{if(t[B-1].getAttribute("total")=="1"){B=t.length-1;}}var C=false;if(h=="2"){a=false;if(f.daoZhi){for(var A=1;A<B;A++){var g=t[A].cells;var n=$(g[0]).text();if(A==B-1){n="平均值";}var d=g.length-1;for(var y=1;y<d;y++){var q=$(g[y]).text();var E=$(t[0].cells[y]).text();var G=parseFloat(q);s.push({name:E,group:n,value:G});}}}else{for(var A=1;A<B;A++){var g=t[A].cells;var E=$(g[0]).text();if(A==B-1){E="平均值";}var d=g.length-1;for(var y=1;y<d;y++){var q=$(g[y]).text();var n=$(t[0].cells[y]).text();var G=parseFloat(q);s.push({name:E,group:n,value:G});}}}}else{if(h=="3"||h=="4"){if(r.height()==300){r.height(400);if(B>5){r.height(600);}}var l=1;if(e){l=2;}for(var A=l;A<B;A++){var g=t[A].cells;var E="";if(e){E=$(t[A-1].cells[0]).text().replace("[详细]","");}else{E=$(g[0]).text().replace("[详细]","");}var d=g.length;if(h=="4"){d=d-1;}if(h=="4"&&m=="3"){a=false;var q=$(g[d]).text();var G=parseFloat(q);s.push({name:E,group:"group",value:G});}else{for(var y=1;y<d;y++){var q=$(g[y]).text();var n=$(t[0].cells[y]).text();var G="";if(g[y].dval){if(f.notPercent){G=parseFloat(g[y].dval);}else{G=parseFloat(g[y].dpercent);}}else{var F=q.split("(");var G=parseFloat(F[0]);if(a){G=parseFloat(F[1].replace(")","").replace("%",""));}}s.push({name:E,group:n,value:G});}}if(e){A++;}}if(B>=6){C=true;}}else{for(var A=1;A<B;A++){if(t[A].style.display=="none"){continue;}var g=t[A].cells;var E=$(g[0]).text().replace("[详细]","");var q=$(g[1]).text();var x=$(g[2]).attr("percent");var G=parseFloat(q);if(a){G=parseFloat(x);}s.push({name:E,group:"group",value:G});}}}var b=null;if(m=="1"){b=HighChart.ChartOptionTemplates.Pie(s,a);}else{if(m=="6"){b=HighChart.ChartOptionTemplates.Pie(s,a,true);}else{if(m=="2"){b=HighChart.ChartOptionTemplates.Bars(s,2,a,r[0].noStack);}else{if(m=="3"){b=HighChart.ChartOptionTemplates.Bars(s,3,a,r[0].noStack);}else{if(m=="4"){b=HighChart.ChartOptionTemplates.Bars(s,4,a,r[0].noStack);}else{if(m=="5"){b=HighChart.ChartOptionTemplates.Bars(s,5,a,r[0].noStack);}}}}}}r.show();var v=r.next();v.show();HighChart.RenderChart(b,r);if(C){if(!r[0].divTip){var o=document.createElement("div");o.style.paddingBottom="5px";o.style.textAlign="center";o.parent=r[0];o.innerHTML="<b>提示：</b>由于此题矩阵小题数量大小等于5题，默认会显示堆叠图，<a href='javascript:' class='link-U00a6e6'>点击显示展开图形</a>";v.after(o);r[0].divTip=o;var u=o.getElementsByTagName("a")[0];u.onclick=function(){var j=this.parentNode.parent;var i=$(j);if(!j.noStack){j.noStack=1;if(i.height()==600){i.height(400);}this.innerHTML="点击显示堆叠图";}else{j.noStack=0;if(i.height()==400){i.height(600);}this.innerHTML="点击显示展开图形";}var J=i.prev().prev();var I=i[0].tableData;if(!I){I=getTable(J.prev());}else{J=i[0].divResultCss;}if(J[0].lastObj){var H=J[0].lastObj;J[0].lastObj=null;$(H).trigger("click");}};}if(m=="2"||m=="4"){r[0].divTip.style.display="";}else{r[0].divTip.style.display="none";}}}$(window).load(function(){initChart();});function openwindow(a,b,c){PDF_launch(a,b,c);}function Display(c,b){if(c.name=="displayChart"){processDiv(b,c);}else{if(c.name=="displayTable"){$.each(divarray,function(){$(this).prev().find("table").toggle();});}else{if(c.name=="displayTableTiao"){$.each(divarray,function(){$(this).prev().find("div.bar").toggle();});}else{if(c.name=="displayValue"){$.each(divarray,function(){var d=$(this).attr("type");if(d=="0"){$(this).prev().find(".avgval").toggle();}else{if(d=="4"){$(this).parent().parent().find(".avgval").toggle();}}});var a=document.getElementById("lblValueTotal");if(a==null){return;}a.style.display=a.style.display==""?"none":"";}}}}}function processDiv(a,b){$.each(divarray,function(){if(!$(this).is(":visible")){return true;}var c=$(this).find("li[index='"+a+"']")[0];if(c){var d=$(c).parent().parent();getTable($(this).prev());if(d[0].lastObj==c&&b.checked){d[0].lastObj=null;}$(c).trigger("click");}});}function getTable(b){var a=b[0].children[0];if(a.tagName.toLowerCase()!="table"){a=b[0].children[1];}return a;}var isExporting=false;function GenerateReport(){if(window.isPub==0){alert("很抱歉，只有问卷发布者才能使用此功能！");return;}if(window.NeedSamplePay){samplePay();return;}var g=0;var q=new Array();q.sort(function(p,i){return p.qIndex-i.qIndex;});var f=new Array();var d=new Array();var n=new Array();var o=new Array();var c=new Array();for(var a in matrixArray){d.push(a);}var m=cbFilter.getElementsByTagName("input");var e="";var b="";if(m){e=m[0].checked?"t":"";b=m[1].checked?"t":"";}var h=document.getElementById("displayTableTiao").checked?"t":"f";var s="";var l=0;var k=false;isExporting=true;$.each(divarray,function(){var x=$(this);var p=$(this).next().next();var w=getTable($(this).prev());var y=$(w).attr("qi");if(w.sortType){n.push(y+";"+w.sortType);}if($(this).is(":visible")){if(!$(w).is(":visible")){f.push(y);}}if(w.removeEmpty){c.push(y);}if(w.notPercent==true||w.notPercent==false){var v=x.attr("type");var u="0";if(w.notPercent){u=1;}if(v=="3"||v=="4"){o.push(y+","+u);}}if(x[0].lastObj){var i=$(p).highcharts();var t=i.getSVGForExport();if(s){s+="¤";}s+=y+"〒"+t;l++;if(l==50){return false;}}});isExporting=false;hfSvg.value=s;if(l>=50){alert("提示：一次最多只级下载50个图片！");}var r="/wjx/activitystat/viewstatsavenew.aspx?activity="+activityId+"&reportId="+reportId+"&fe="+e+"&fj="+b+"&dtt="+h;if(k){r+="&bs64=1";}r+="&t="+f.join(",")+"&m="+d.join(",");if(n.length>0){r+="&st="+n.join(",");}if(o.length>0){r+="&pa="+o.join(";");}if(c.length>0){r+="&re="+c.join(",");}if(qCond){if(reportType==3){cond="&arc=";}else{cond="&qc=";}cond+=encodeURIComponent(qCond);}else{cond="&qc=";}if(eCond){if(reportType==3){cond+="&aec=";}else{cond+="&ec=";}cond+=encodeURIComponent(eCond);}if(reportName){var j=reportName.replace(/\(/g,"（").replace(/\)/g,"）");cond+="&name="+encodeURIComponent(j);}r+=cond+"&reporttype="+reportType;PDF_launch(r,600,320);return;}var matrixArray=new Object();function ShowMatrix(f,d){var a="divDetail"+f;var c=document.getElementById(a);c.style.display=c.style.display=="none"?"":"none";d.innerHTML=c.style.display=="none"?"查看详细数据":"查看总体数据";var b="divTotal"+f;var g=document.getElementById(b);g.style.display=g.style.display=="none"?"":"none";var e=parseInt(f)*10000;if(matrixArray[e]){delete matrixArray[e];}else{matrixArray[e]=a;}}function sortTable(b,f,l,e){var c=(typeof(b)=="object"?b:document.getElementById(b));if(c.reverseSort==null){c.reverseSort=new Array();c.lastColumn=2;}if(c.reverseSort[f]==null){c.reverseSort[f]=l;}else{c.reverseSort[f]=!c.reverseSort[f];}c.lastColumn=f;var a=c.style.display;var d;var h,g;var o,k;var p;var n;var m=c.rows.length;if(e){m=m-1;}for(h=1;h<m-1;h++){k=h;o=getTextValue(c.rows[h].cells[f]);for(g=h+1;g<m;g++){p=getTextValue(c.rows[g].cells[f]);n=compareValues(o,p);if(c.reverseSort[f]){n=-n;}if(n>0){k=g;o=p;}}if(k>h){d=c.removeChild(c.rows[k]);c.insertBefore(d,c.rows[h]);}}return false;}if(document.ELEMENT_NODE==null){document.ELEMENT_NODE=1;document.TEXT_NODE=3;}function getTextValue(c){var d=c.getAttribute("val");if(d){return d;}var a;var b;b="";for(a=0;a<c.childNodes.length;a++){if(c.childNodes[a].nodeType==document.TEXT_NODE){b+=c.childNodes[a].nodeValue;}else{if(c.childNodes[a].nodeType==document.ELEMENT_NODE&&c.childNodes[a].tagName=="BR"){b+=" ";}else{b+=getTextValue(c.childNodes[a]);}}}return normalizeString(b);}function compareValues(d,b){var a,c;a=parseFloat(d);c=parseFloat(b);if(!isNaN(a)&&!isNaN(c)){d=a;b=c;}if(d==b){return 0;}if(d>b){return 1;}return -1;}var whtSpEnds=new RegExp("^\\s*|\\s*$","g");var whtSpMult=new RegExp("\\s\\s+","g");function normalizeString(a){a=a.replace(whtSpMult," ");a=a.replace(whtSpEnds,"");return a;}var rowClsNm="alternateRow";var colClsNm="sortedColumn";var rowTest=new RegExp(rowClsNm,"gi");var colTest=new RegExp(colClsNm,"gi");function makePretty(g,d){var e,c;var b,a;for(e=0;e<g.rows.length;e++){b=g.rows[e];b.className=b.className.replace(rowTest,"");if(e%2!=0){b.className+=" "+rowClsNm;}b.className=normalizeString(b.className);for(c=2;c<g.rows[e].cells.length;c++){a=b.cells[c];a.className=a.className.replace(colTest,"");if(c==d){a.className+=" "+colClsNm;}a.className=normalizeString(a.className);}}var f=g.parentNode.tHead;b=f.rows[f.rows.length-1];for(e=2;e<b.cells.length;e++){a=b.cells[e];a.className=a.className.replace(colTest,"");if(e==d){a.className+=" "+colClsNm;}a.className=normalizeString(a.className);}}function setRanks(a,e,k){var j=0;var b=1;if(a.reverseSort[e]){k=!k;}if(k){b=-1;j=a.rows.length-1;}var l=1;var h=l;var m;var d=null;while(e>1&&j>=0&&j<a.rows.length){m=getTextValue(a.rows[j].cells[e]);if(d!=null&&compareValues(m,d)!=0){h=l;}a.rows[j].rank=h;d=m;l++;j+=b;}var g,c;var f=0;for(j=0;j<a.rows.length;j++){g=a.rows[j];c=g.cells[0];while(c.lastChild!=null){c.removeChild(c.lastChild);}if(e>1&&g.rank!=f){c.appendChild(document.createTextNode(g.rank));f=g.rank;}}}