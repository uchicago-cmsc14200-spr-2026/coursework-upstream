Your implementation of the ConnectMStub class (in fakes.py) should return valid constants for every method.

To test the TUI with the stubbed implementation, run:

    python3 mini-tui.py stub

Your implementation of the ConnectMFake class (in fakes.py) should:

- Store the full board internally, but only ever modify the bottom row of the board.
- Check whether a piece can be dropped by only checking whether there is a value in the bottom row or not.
- Drop a piece by setting a value in that row.
- After M moves, set the winner to be YELLOW if M is odd, and RED if it is even.

To test the TUI with the faked implementation, run:

    python3 mini-tui.py fake