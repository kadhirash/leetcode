package main
func trap(height []int) int {
    var water, lowestSide, leftHeight, rightHeight int
    maxHeight, maxPos := getHeighestBar(height)
    for i := 0; i < maxPos; i++ {
        lowestSide = Min(leftHeight, maxHeight)
        if lowestSide > height[i] {
            water += lowestSide - height[i]
        }
        if height[i] > leftHeight {
            leftHeight = height[i]
        }
    }
    for i := len(height)-1; i >= maxPos; i-- {
        lowestSide = Min(rightHeight, maxHeight)
        if lowestSide > height[i] {
            water += lowestSide - height[i]
        }
        if height[i] > rightHeight {
            rightHeight = height[i]
        }
    }
    return water
}

func getHeighestBar(height []int) (maxHeight, maxPos int) {
    for i, h := range height {
        if h > maxHeight {
            maxHeight = h
            maxPos = i
        }
    }
    return
}

func Min(x, y int) int {
    if x < y {
        return x
    }
    return y
}