def fd_payout(
    p : float, t : int, r : float, c : int
):
    
    '''
    Calculate fixed deposit 
    Inputs:  principal, term in years, rate as a decimal, compunding period(compund after how many months)
    Ouput: fixed deposit payout for monthly, yearly and cumulative compounding 
    '''
    try:
        payout = functions.fd_payout(
            p, t, r, c
        )
        return {
            "Tag": "fd_payout",
            "Principal": p,
            "Term (in years)": t,
            "Rate (as a decimal)" : r,
            "Compounding period" : c,
            "Payout_monthly": payout[0],
            "Payout_yearly": payout[1],
            "Payout_cumulative": payout[2],
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
