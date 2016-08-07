module LeapYear (isLeapYear) where

isLeapYear :: Int -> Bool
isLeapYear year
    | year `mod` 400 == 0   = True
    | year `mod` 100 == 0   = False
    | otherwise             = mod year 4 == 0
