sol :: [Int] -> Int -> Int
sol ls n = foldr (\(a,b) s -> if a<b then s+1 else s) 0 $ zip ls $ drop n ls

main = do
    file <- readFile "input.txt"
    let xs = map read (lines file) :: [Int]
    putStrLn $ "Star 1: " ++ (show $ sol xs 1)
    putStrLn $ "Star 2: " ++ (show $ sol xs 3)
