import 'dart:ui';

class AppStyling {
  final double horizontalPagePadding = 128.0;
  final double verticalPagePadding = 200.0;
  final double horizontalPageDiscountPadding = 50.0;
  final double sizeBetweenSections = 50.0;
  final Color codeKeywordColor = Color(0xFF38BB36);
  final Color codeStringColor = Color(0xFFF8C43F);
  final double markerSize = 25.0;
  final double codeWindowWidth = 500.0;
  final double codeWindowFrameHeight = 35.0;

  double get discountedHorizontalPagePadding => horizontalPagePadding - horizontalPageDiscountPadding;
  double get discountedHorizontalMarkerPadding => discountedHorizontalPagePadding - ((markerSize + 1) * 2);
}