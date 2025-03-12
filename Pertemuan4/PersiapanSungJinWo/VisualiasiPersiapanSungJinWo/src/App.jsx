import React, { useState, useEffect } from 'react';

const App = () => {
  const [step, setStep] = useState(0);
  const [speed, setSpeed] = useState(1000);
  const [isPlaying, setIsPlaying] = useState(false);
  const [highlightedIndices, setHighlightedIndices] = useState([]);
  const [posMapping, setPosMapping] = useState({});
  const [convertedList, setConvertedList] = useState([]);
  const [validCombinations, setValidCombinations] = useState([]);
  const [currentCombination, setCurrentCombination] = useState(null);
  const [isValid, setIsValid] = useState(null);
  
  const nums1 = [2, 0, 1, 3];
  const nums2 = [0, 1, 2, 3];
  
  const totalSteps = 15; // Adjusted based on visualization needs
  
  const resetAnimation = () => {
    setStep(0);
    setHighlightedIndices([]);
    setPosMapping({});
    setConvertedList([]);
    setValidCombinations([]);
    setCurrentCombination(null);
    setIsValid(null);
  };
  
  const togglePlay = () => {
    setIsPlaying(!isPlaying);
  };
  
  const handleStepChange = (newStep) => {
    if (newStep >= 0 && newStep <= totalSteps) {
      setStep(newStep);
    }
  };
  
  useEffect(() => {
    if (!isPlaying) return;
    
    const timer = setTimeout(() => {
      if (step < totalSteps) {
        setStep(step + 1);
      } else {
        setIsPlaying(false);
      }
    }, speed);
    
    return () => clearTimeout(timer);
  }, [step, isPlaying, speed]);
  
  useEffect(() => {
    // Reset states
    setHighlightedIndices([]);
    setPosMapping({});
    setConvertedList([]);
    setCurrentCombination(null);
    setIsValid(null);
    
    // Step 1: Show the original arrays
    if (step === 0) {
      // Nothing to highlight yet
    } 
    // Step 2: Mapping positions in nums2
    else if (step === 1) {
      const mapping = {};
      nums2.forEach((num, idx) => {
        mapping[num] = idx;
      });
      setPosMapping(mapping);
    } 
    // Step 3: Convert nums1 to positions in nums2
    else if (step === 2) {
      const mapping = {};
      nums2.forEach((num, idx) => {
        mapping[num] = idx;
      });
      setPosMapping(mapping);
      const converted = nums1.map(num => mapping[num]);
      setConvertedList(converted);
    }
    // Steps 4-15: Check combinations
    else if (step >= 3 && step <= totalSteps) {
      const combinations = [
        [0, 1, 2], // (2,0,1)
        [0, 1, 3], // (2,0,3)
        [0, 2, 3], // (2,1,3)
        [1, 2, 3]  // (0,1,3)
      ];
      
      const combinationIndex = step - 3;
      if (combinationIndex < combinations.length) {
        const [i, j, k] = combinations[combinationIndex];
        setHighlightedIndices([i, j, k]);
        setCurrentCombination([nums1[i], nums1[j], nums1[k]]);
        
        const mapping = {};
        nums2.forEach((num, idx) => {
          mapping[num] = idx;
        });
        const converted = nums1.map(num => mapping[num]);
        
        const isValidCombo = converted[i] < converted[j] && converted[j] < converted[k];
        setIsValid(isValidCombo);
        
        if (isValidCombo) {
          setValidCombinations(prev => [...prev, [nums1[i], nums1[j], nums1[k]]]);
        }
      }
    }
  }, [step]);
  
  return (
    <div className="flex flex-col items-center w-full p-4 bg-gray-50 rounded-lg">
      <h1 className="text-xl font-bold mb-4">Increasing Subsequence Visualization</h1>
      
      <div className="w-full flex justify-center mb-6">
        <div className="flex flex-col items-center mx-4">
          <div className="font-semibold mb-2">nums1 (power order)</div>
          <div className="flex">
            {nums1.map((num, idx) => (
              <div 
                key={`nums1-${idx}`} 
                className={`w-12 h-12 flex items-center justify-center border ${
                  highlightedIndices.includes(idx) ? 'bg-blue-200 border-blue-500' : 'bg-white border-gray-300'
                } m-1 rounded`}
              >
                {num}
              </div>
            ))}
          </div>
          <div className="flex mt-1">
            {nums1.map((_, idx) => (
              <div key={`idx1-${idx}`} className="w-12 flex justify-center m-1 text-xs text-gray-500">
                idx: {idx}
              </div>
            ))}
          </div>
        </div>
        
        <div className="flex flex-col items-center mx-4">
          <div className="font-semibold mb-2">nums2 (price order)</div>
          <div className="flex">
            {nums2.map((num, idx) => (
              <div 
                key={`nums2-${idx}`} 
                className={`w-12 h-12 flex items-center justify-center border ${
                  Object.entries(posMapping).some(([key, value]) => parseInt(key) === num && highlightedIndices.some(i => nums1[i] === parseInt(key)))
                    ? 'bg-green-200 border-green-500' : 'bg-white border-gray-300'
                } m-1 rounded`}
              >
                {num}
              </div>
            ))}
          </div>
          <div className="flex mt-1">
            {nums2.map((_, idx) => (
              <div key={`idx2-${idx}`} className="w-12 flex justify-center m-1 text-xs text-gray-500">
                pos: {idx}
              </div>
            ))}
          </div>
        </div>
      </div>
      
      {(step >= 1) && (
        <div className="w-full max-w-md p-4 border rounded bg-white mb-4">
          <h2 className="font-semibold mb-2">Position mapping in nums2:</h2>
          <div className="flex flex-wrap">
            {Object.entries(posMapping).map(([key, value]) => (
              <div key={`map-${key}`} className="m-1 p-2 bg-gray-100 rounded">
                Value {key} → Position {value}
              </div>
            ))}
          </div>
        </div>
      )}
      
      {(step >= 2) && (
        <div className="w-full max-w-md p-4 border rounded bg-white mb-4">
          <h2 className="font-semibold mb-2">nums1 converted to positions in nums2:</h2>
          <div className="flex justify-center">
            {nums1.map((num, idx) => (
              <div key={`orig-${idx}`} className="flex flex-col items-center m-2">
                <div className="w-12 h-12 flex items-center justify-center border bg-blue-100 rounded mb-1">
                  {num}
                </div>
                <div className="w-12 h-12 flex items-center justify-center border bg-green-100 rounded">
                  {convertedList[idx]}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
      
      {(step >= 3) && currentCombination && (
        <div className={`w-full max-w-md p-4 border rounded mb-4 ${isValid ? 'bg-green-50' : 'bg-red-50'}`}>
          <h2 className="font-semibold mb-2">Checking combination:</h2>
          <div className="flex justify-center mb-2">
            {currentCombination.map((num, idx) => (
              <div key={`comb-${idx}`} className="w-12 h-12 flex items-center justify-center border bg-blue-100 m-1 rounded">
                {num}
              </div>
            ))}
          </div>
          <div className="text-center">
            {isValid ? (
              <span className="text-green-600 font-medium">✓ Valid combination! Increasing in both lists.</span>
            ) : (
              <span className="text-red-600 font-medium">✗ Invalid combination. Not increasing in both lists.</span>
            )}
          </div>
        </div>
      )}
      
      {(validCombinations.length > 0) && (
        <div className="w-full max-w-md p-4 border rounded bg-green-50 mb-4">
          <h2 className="font-semibold mb-2">Valid combinations found: {validCombinations.length}</h2>
          <div className="flex flex-col">
            {validCombinations.map((combo, idx) => (
              <div key={`valid-${idx}`} className="flex justify-center my-1 p-2 bg-white rounded">
                {combo.map((num, i) => (
                  <div key={`valid-${idx}-${i}`} className="w-12 h-12 flex items-center justify-center border bg-green-100 m-1 rounded">
                    {num}
                  </div>
                ))}
              </div>
            ))}
          </div>
        </div>
      )}
      
      <div className="w-full max-w-md flex flex-col items-center mt-4">
        <div className="text-center mb-4">
          Step {step} of {totalSteps}: {getStepDescription(step)}
        </div>
        
        <div className="flex items-center w-full justify-center">
          <button 
            onClick={() => handleStepChange(step - 1)} 
            disabled={step === 0}
            className="px-4 py-2 bg-gray-200 rounded disabled:opacity-50 mr-2"
          >
            Previous
          </button>
          
          <button 
            onClick={togglePlay} 
            className="px-4 py-2 bg-blue-500 text-white rounded mx-2"
          >
            {isPlaying ? 'Pause' : 'Play'}
          </button>
          
          <button 
            onClick={() => handleStepChange(step + 1)} 
            disabled={step === totalSteps}
            className="px-4 py-2 bg-gray-200 rounded disabled:opacity-50 ml-2"
          >
            Next
          </button>
        </div>
        
        <button 
          onClick={resetAnimation} 
          className="px-4 py-2 bg-red-500 text-white rounded mt-4"
        >
          Reset
        </button>
        
        <div className="w-full mt-4">
          <label className="block mb-2">Animation Speed:</label>
          <input 
            type="range" 
            min="200" 
            max="2000" 
            step="100" 
            value={speed} 
            onChange={(e) => setSpeed(parseInt(e.target.value))}
            className="w-full"
          />
          <div className="flex justify-between">
            <span>Fast</span>
            <span>Slow</span>
          </div>
        </div>
      </div>
    </div>
  );
};

function getStepDescription(step) {
  switch(step) {
    case 0: return "Original arrays";
    case 1: return "Create position mapping for nums2";
    case 2: return "Convert nums1 to positions in nums2";
    case 3: return "Check combination (2,0,1)";
    case 4: return "Check combination (2,0,3)";
    case 5: return "Check combination (2,1,3)";
    case 6: return "Check combination (0,1,3)";
    default: return "Analysis complete";
  }
}

export default App;