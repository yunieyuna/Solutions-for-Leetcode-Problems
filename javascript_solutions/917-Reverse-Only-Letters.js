/* Question Link: https://leetcode.com/problems/reverse-only-letters/ */

/**
 * @param {string} S
 * @return {string}
 */
const isValidStr = (str) => {
    return /^[a-zA-Z]+$/.test(str)
}

var reverseOnlyLetters = function(S) {
    // Two Pointers
    let strArr = S.split('')

    let start = 0
    let end = strArr.length - 1

    while(start < end){
        // if curStartCharacter and curEndCharacter are valid
        // then I need to swap and then increment/decrement start and end
        // if curStartCharacter or curEndCharacter is not valid
        // I will skip it
        const startLetter = strArr[start]
        const endLetter = strArr[end]
        const isStartLetterValid = isValidStr(startLetter)
        const isEndLetterValid = isValidStr(endLetter)

        if (isStartLetterValid && isEndLetterValid) {
            strArr[start] = endLetter
            strArr[end] = startLetter
            start += 1
            end -= 1
        }

        if (!isStartLetterValid) {
            start += 1
        }

        if (!isEndLetterValid) {
            end -= 1
        }
    }
    return strArr.join('')
};
