# Stock Portfolio Optimization System

Implemented the fundamental concept of diversification and created a portfolio optimization system that generates a portfolio having the maximum return-to-risk ratio (sharpe ratio) incorporating Monte Carlo Simulations for optimal weights of stocks.

The Monte Carlo Simulation is used to generate a set of predicted returns for the portfolio of assets which will help to find out the Value at Risk (VaR) of investments and to get the optimal weights for the stocks.

To simplify the analysis, we deal with daily returns and standard deviation and will consider only 1 month of stock data. The formulae for converting daily returns and standard deviation to an annual basis are as shown (assuming 252 trading days in a year):

                                    Annual Return = Daily Return * 252
                                    Annual Standard Deviation = Daily Standard Deviation * 252
                       
Assign random weights to all stocks, keeping the sum of the weights to be 1. We will compute the return and standard deviation of the portfolio. Then run Monte Carlo Simulations on portfolio to get the optimal weights for stocks. At every particular combination of these weights, we compute the return and standard deviation of the portfolio and save it. We’ll then change the weights and assign some random values and repeat the above procedure for number of iterations. Higher the number of iterations, higher will be the accuracy of the optimization but at the cost of computation and time.
