"""
==========================================================================
Phi.py
==========================================================================
Functional unit Phi for CGRA tile.

Author : Cheng Tan
  Date : November 30, 2019

"""

from pymtl3 import *
from pymtl3.stdlib.ifcs import SendIfcRTL, RecvIfcRTL
from ...lib.opt_type    import *
from ..basic.Fu         import Fu

class Phi( Fu ):

  def construct( s, DataType, ConfigType ):

    super( Phi, s ).construct( DataType, ConfigType )

    @s.update
    def comb_logic():
      assert( not (s.recv_in0.msg.predicate==Bits1(1) and\
                   s.recv_in1.msg.predicate==Bits1(1)) )
      if s.recv_opt.msg.ctrl == OPT_PHI:
        if s.recv_in0.msg.predicate == Bits1( 1 ):
          s.send_out0.msg = s.recv_in0.msg
        elif s.recv_in1.msg.predicate == Bits1( 1 ):
          s.send_out0.msg = s.recv_in1.msg

  def line_trace( s ):
    symbol0 = "#"
    symbol1 = "#"
    if s.recv_in0.msg.predicate == Bits1(1):
      symbol0 = "*"
      symbol1 = " "
    elif s.recv_in1.msg.predicate == Bits1(1):
      symbol0 = " "
      symbol1 = "*"
    return f'[{s.recv_in0.msg} {symbol0}] [{s.recv_in1.msg} {symbol1}] = [{s.send_out0.msg}]'
