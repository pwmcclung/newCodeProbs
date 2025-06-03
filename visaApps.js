function visa(applicants) {
    const today = new Date();
    const approvedApplicants = [];
  
    const pad = (num) => num.toString().padStart(2, "0"); 
  
    for (const applicant of applicants) {
      const [day, month, year] = applicant.passportExpiration.split(".").map(Number);
      const passportExpiryDate = new Date(year, month - 1, day); 
      const diffTime = passportExpiryDate - today;
      const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  
      if (applicant.criminalRecord || diffDays < 90) {
        continue; 
      }
  
      let insuranceId = 0;
      for (let i = 0; i < applicant.firstName.length; i++) {
        insuranceId += applicant.firstName.charCodeAt(i);
      }
      for (let i = 0; i < applicant.lastName.length; i++) {
        insuranceId += applicant.lastName.charCodeAt(i);
      }
  
      //Set visaExpiration with leading zeros
      let visaExpiryDate;
      if (applicant.visaType === "business") {
        visaExpiryDate = new Date(today);
        visaExpiryDate.setDate(today.getDate() + 90);
      } else {
        visaExpiryDate = new Date(today);
        visaExpiryDate.setDate(today.getDate() + 30);
      }
  
      const formattedVisaExpiry = `${pad(visaExpiryDate.getDate())}.${pad(visaExpiryDate.getMonth() + 1)}.${visaExpiryDate.getFullYear()}`;
  
      approvedApplicants.push({
        ...applicant,
        visaExpiration: formattedVisaExpiry,
        insuranceId: insuranceId,
      });
    }
  
    return approvedApplicants;
  }