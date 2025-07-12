def longer(st): 
    return ' '.join(sorted(st.split(), key=lambda x: (len(x), x)))