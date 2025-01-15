/**
 * Constructor DependencyInjector
 * @param {Object} - object with dependencies
 */
var DI = function (dependency) {
    this.dependency = dependency;
  };
  
  DI.prototype.inject = function (func) {
    const dependencies = this.dependency;
  
    return function() {
      const FN_ARGS = /^function\s*[^\(]*\(\s*([^\)]*)\)/m;
      const FN_ARG_SPLIT = /,/;
      const FN_ARG = /^\s*(_?)(\S+?)\1\s*$/;
      const STRIP_COMMENTS = /((\/\/.*$)|(\/\*[\s\S]*?\*\/))/mg;
  
      let argNames = [];
      const argsMatch = func.toString().replace(STRIP_COMMENTS, '').match(FN_ARGS);
      if (argsMatch && argsMatch[1].trim() !== '') { 
          argNames = argsMatch[1].split(FN_ARG_SPLIT);
      }
  
  
      const resolvedDependencies = argNames.map(argName => {
        const name = argName.trim();
        return dependencies[name];
      });
  
      return func.apply(this, resolvedDependencies);
    };
  };