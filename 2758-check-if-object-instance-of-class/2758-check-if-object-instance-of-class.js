/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    // Handle invalid classFunction
    if (classFunction == null || typeof classFunction !== 'function') return false;
    
    // Handle null or undefined obj
    if (obj == null) return false;
    
    // Handle primitives by mapping to their wrapper classes
    const primitiveToWrapper = {
        'number': Number,
        'string': String,
        'boolean': Boolean,
        'symbol': Symbol,
        'bigint': BigInt
    };
    
    const objType = typeof obj;
    if (objType in primitiveToWrapper) {
        // For primitives, create a temporary wrapper object to check inheritance
        const wrapper = primitiveToWrapper[objType];
        // Check if the wrapper's prototype inherits from classFunction
        return wrapper.prototype instanceof classFunction || wrapper === classFunction;
    }
    
    // Handle objects using instanceof
    return obj instanceof classFunction;
};