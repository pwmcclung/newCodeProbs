function match(job, candidates) {
    return candidates.filter(candidate => {
      let equityMatch = job.equityMax > 0 || !candidate.desiresEquity;
      let locationMatch = job.locations.some(location => 
        location === candidate.currentLocation || candidate.desiredLocations.includes(location)
      );
      return equityMatch && locationMatch;
    });
  }