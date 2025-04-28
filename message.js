function validate(message){
  let pattern = /^MDZHB \d{2} \d{3} [A-Z]+ \d{2} \d{2} \d{2} \d{2}$/;
  return pattern.test(message);
	}
