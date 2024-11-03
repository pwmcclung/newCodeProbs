function romanize(cyrillic) {
    let changer = {'':'','А':'a','а':'a','Б':'b','б':'b','В':'v','в':'v','Г':'g','г':'g','Д':'d', 'д':'d', 
                  'Е':'e','е':'e','Ё':'e','ё':'e','Ж':'zh','ж': 'zh','З':'z' ,'з': 'z','И':'i','и': 'i','Й':'i','й': 'i',
                  'К':'k' ,'к': 'k','Л':'l' ,'л': 'l','М':'m' ,'м':'m','Н': 'n'	,'н': 'n','О':'o','о': 'o',
                  'П':'p'	,'п': 'p','Р':'r','р':'r','С': 's','с': 's','Т': 't'	,'т': 't','У':'u','у': 'u','Ф':'f','ф': 'f',
                  'Х':'kh' 	,'х':'kh','Ц':'ts' 	,'ц': 'ts','Ч':'ch','ч': 'ch','Ш': 'sh','ш': 'sh','Щ':'shch','щ':'shch','Ъ': 'ie'	,
                   'ъ':'ie','Ы': 'y','ы': 'y','Ь':'','ь': '','Э': 'e'	,'э': 'e','Ю':'iu' ,'ю': 'iu','Я':'ia','я': 'ia'}
    let cyrSplit = cyrillic.split(' ');
    let first = cyrSplit[0].split('').map((x) => changer[x]).join('');
    let second = cyrSplit[1].split('').map((x) => changer[x]).join('');
    let firstName = String(first.slice(0,1)).toUpperCase() + first.slice(1,);
    let secondName = String(second.slice(0,1)).toUpperCase() + second.slice(1,);
    return `${firstName} ${secondName}`;
    }