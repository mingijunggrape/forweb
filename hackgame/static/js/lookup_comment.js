function fn_checkByte(obj){
    const maxByte = 3000; //최대 100바이트
    const text_val = obj.value; //입력한 문자
    const text_len = text_val.length; //입력한 문자수
    
    let totalByte=0;
    let strlen;
    for(let i=0; i<text_len; i++){
    	const each_char = text_val.charAt(i);
        const uni_char = escape(each_char) //유니코드 형식으로 변환
        if(uni_char.length>4){
        	// 한글 : 2Byte
            totalByte += 2;
        }else{
        	// 영문,숫자,특수문자 : 1Byte
            totalByte += 1;
        }

        if(totalByte <= 3000)
        {
            strlen = i+1;                                          //return할 문자열 갯수
        }
    }
    
    if(totalByte>maxByte){
            let str2 = "";
            str2 =  text_val.substr(0,strlen); 
            console.log(str2)
    	    alert('최대 3000Byte까지만 입력가능합니다.');
        	document.getElementById("nowByte").innerText = totalByte;
            document.getElementById("nowByte").style.color = "red";
            obj.value = str2;
            
        }else{
        	document.getElementById("nowByte").innerText = totalByte;
            document.getElementById("nowByte").style.color = "green";
        }
    }