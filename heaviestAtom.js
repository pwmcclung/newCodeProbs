const Spectrometer = {
    getHeaviest: function(atomicMasses) {
      if (!atomicMasses || atomicMasses.length === 0) return 0; 
      let heaviest = atomicMasses[0];
      for (let i = 1; i < atomicMasses.length; i++) {
        if (atomicMasses[i] > heaviest) {
          heaviest = atomicMasses[i];
        }
      }
      return heaviest;
    }
  };