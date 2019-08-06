static JSONObject cursorToJson(Cursor c) {
    JSONObject retVal = new JSONObject();
    for(int i=0; i<c.getColumnCount(); i++) {
        String cName = c.getColumnName(i);
        try {
            switch (c.getType(i)) {
                case Cursor.FIELD_TYPE_INTEGER:
                    retVal.put(cName, c.getInt(i));
                    break;
                case Cursor.FIELD_TYPE_FLOAT:
                    retVal.put(cName, c.getFloat(i));
                    break;
                case Cursor.FIELD_TYPE_STRING:
                    retVal.put(cName, c.getString(i));
                    break;
                case Cursor.FIELD_TYPE_BLOB:
                    retVal.put(cName, DataUtils.bytesToHexString(c.getBlob(i)));
                    break;
            }
        }
        catch(Exception ex) {
            Log.e(TAG, "Exception converting cursor column to json field: " + cName);
        }
    }
    return retVal;
}

